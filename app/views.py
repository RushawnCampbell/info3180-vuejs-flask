"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db, login_manager
from flask import request, jsonify, send_file, send_from_directory
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
from app.models import Users
from app.models import Cars
from app.models import Favourites
from app.forms import LoginForm
from app.forms import RegisterForm
from app.forms import CarForm
from flask_wtf.csrf import generate_csrf
from werkzeug.utils import secure_filename
import os
import datetime 
import jwt
import locale
import json
locale.setlocale( locale.LC_ALL, 'en_CA.UTF-8' )


###
# Routing for your application.
###

@app.route('/')
def index():
    return send_file(os.path.join('../dist/', 'index.html'))


@app.route('/api/register', methods=['POST'])
def register():
    
    if request.method == 'POST':
        formobject =  RegisterForm()
        if formobject.validate_on_submit():
            fileobj = request.files['photo']
            cleanedname = secure_filename(fileobj.filename)
            fileobj.save(os.path.join(app.config['UPLOAD_FOLDER'], cleanedname))
            if fileobj and (cleanedname != "" and cleanedname != " "):
                date_joined = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                newuser = Users(formobject.username.data,formobject.password.data, formobject.fullname.data, formobject.email.data,formobject.location.data, formobject.biography.data, cleanedname, date_joined )
                db.session.add(newuser)
                db.session.commit()
                userid =  db.session.query(Users.id).all()[-1][0]
                feedback= {
                        "id": userid,
                        "username": formobject.username.data,
                        "name": formobject.fullname.data,
                        "photo": cleanedname,
                        "email": formobject.email.data,
                        "location": formobject.location.data,
                        "biography": formobject.biography.data,
                        "date_joined": date_joined
                    }
                return jsonify(feedback),201
        return jsonify(form_errors(formobject)),200  

@app.route('/api/auth/login', methods=['POST'])
def login():
    loginform = LoginForm()
    if request.method == "POST":
        if  loginform.validate_on_submit():
            username = loginform.username.data
            password = loginform.password.data
            user = Users.query.filter_by(username=username).first()
            if user is not None and check_password_hash(user.password, password):
                login_user(user)
                tokencreationtime = datetime.datetime.utcnow().strftime("%H:%M:%S")
                token  = jwt.encode({'sub':username,'initime': tokencreationtime}, app.config.get('SECRET_KEY'),algorithm='HS256')
                return jsonify({
                        "message": "Login Successful",
                        "token": token
                    }),200
            else:
                return jsonify({
                        "message": "Login failed, check your information and try again.",
                    }),401
                   

@app.route('/api/auth/logout', methods=['GET'])
@login_required
def logout():
        if request.method == 'GET':
            logout_user()
            return jsonify({
                "message": "Log out successful"
            }),200

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

@app.route('/api/cars', methods=['GET', 'POST'])
@login_required
def cars():
    user_token= request.headers['Authorization'].split(' ')[1]
    
    if not user_token:
        return jsonify({"message": "Access token is missing or invalid"}),401
    try:
        decoded = jwt.decode(user_token, app.config['SECRET_KEY'], algorithms=['HS256'])
        if decoded['sub'] == current_user.username:
            if request.method == "GET":
                cars = []
                returnedcars = Cars.query.all()
                for car in returnedcars:
                    cars.append({
                        "id": car.id,
                        "description": car.description,
                        "year": car.year,
                        "make": car.make,
                        "model": car.model,
                        "colour": car.colour,
                        "transmission": car.transmission,
                        "car_type": car.car_type,
                        "price": locale.currency(car.price, grouping= True),
                        "photo": car.photo,
                        "user_id": current_user.id
                    })
                if len(cars) >=  3:
                    cars = [cars[-3], cars[-2], cars[-1]]
                return jsonify(cars),200
            elif request.method == "POST":
                formobject =  CarForm()
                if formobject.validate_on_submit():
                    fileobj = request.files['photo']
                    cleanedname = secure_filename(fileobj.filename)
                   
                    fileobj.save(os.path.join(app.config['UPLOAD_FOLDER'], cleanedname))
                    if fileobj and (cleanedname != "" and cleanedname != " "):
                        newcar = Cars(formobject.description.data, formobject.make.data, formobject.model.data,formobject.colour.data, formobject.year.data, formobject.transmission.data, formobject.car_type.data, formobject.price.data, cleanedname, current_user.id )
                        db.session.add(newcar)
                        db.session.commit()
                        feedback = {
                            "description": formobject.description.data,
                            "year": formobject.year.data,
                            "make": formobject.make.data,
                            "model": formobject.model.data,
                            "colour": formobject.colour.data,
                            "transmission": formobject.transmission.data,
                            "type": formobject.car_type.data,
                            "price": formobject.price.data,
                            "photo": cleanedname,
                            "user_id": current_user.id
                        }
                        return jsonify(feedback),201
                return jsonify(form_errors(formobject)),200 
                        
    except:
        return jsonify({"message": "Access token is missing or invalid"}),401

@app.route('/api/cars/<int:car_id>', methods=['GET'])
@login_required
def singlecar(car_id):

    user_token= request.headers['Authorization'].split(' ')[1]
    if not user_token:
        return jsonify({"message": "Access token is missing or invalid"}),401
    try:
        decoded = jwt.decode(user_token, app.config['SECRET_KEY'], algorithms=['HS256'])
        if decoded['sub'] == current_user.username:
            if request.method == 'GET':
                returnedcar = Cars.query.filter_by(id=car_id).first()
                car = {
                    "id": returnedcar.id,
                    "description": returnedcar.description,
                    "year": returnedcar.year,
                    "make": returnedcar.make,
                    "model": returnedcar.model,
                    "colour": returnedcar.colour,
                    "transmission": returnedcar.transmission,
                    "car_type": returnedcar.car_type,
                    "price": locale.currency(returnedcar.price, grouping= True),
                    "photo": returnedcar.photo,
                    "user_id": returnedcar.user_id
                }
            return jsonify(car),200
    except:
        return jsonify({"message": "Access token is missing or invalid"}),401

@app.route('/api/cars/<int:car_id>/favourite', methods=["POST"])
@login_required
def favourite(car_id):
    user_token= request.headers['Authorization'].split(' ')[1]
    if not user_token:
        return jsonify({"message": "Access token is missing or invalid"}),401
    try:
        decoded = jwt.decode(user_token, app.config['SECRET_KEY'], algorithms=['HS256'])
        if decoded['sub'] == current_user.username:
            if request.method == "POST":
                car = json.loads(request.data)
                current_favorites = Favourites.query.all()
                for fave in current_favorites:
                    if fave.user_id == int(car['user_id'])  and fave.car_id == car['car_id']:
                        Favourites.query.filter_by(car_id=car['car_id'], user_id = int(car['user_id']) ).delete()
                        db.session.commit()
                        return jsonify({"message": "Car removed from Favourites"}),201
                    
                favourite = Favourites(car['car_id'], car['user_id'])
                db.session.add(favourite)
                db.session.commit()
                feedback = {
                    "message": "Car Successfully Favourited",
                    "car_id": car['car_id']
                }
                return jsonify(feedback),200
    except:
        return jsonify({"message": "Access token is missing or invalid"}),401

@app.route('/api/search', methods=['GET'])
@login_required
def search():
    user_token= request.headers['Authorization'].split(' ')[1]
    if not user_token:
        return jsonify({"message": "Access token is missing or invalid"}),401
    try:
        decoded = jwt.decode(user_token, app.config['SECRET_KEY'], algorithms=['HS256'])
        if decoded['sub'] == current_user.username:
            if request.method == 'GET':
                params = request.args
                makedata = params.get('searchmake')
                modeldata = params.get('searchmodel')
                cars= []
                if makedata != '' and modeldata !='':
                    searchedcars = Cars.query.filter_by(make = makedata).all()
                    
                if makedata != '' and modeldata == '':
                    searchedcars = Cars.query.filter_by(make = makedata).all()

                if makedata == '' and modeldata != '':
                    searchedcars = Cars.query.filter_by(model = modeldata).all()
                
                if makedata == '' and modeldata =='':
                    searchedcars = Cars.query.all()
                
                for car in searchedcars:

                    if car in cars:
                        continue
                    cars.append(
                        {
                            "id": car.id,
                            "description": car.description,
                            "year": car.year,
                            "make": car.make,
                            "model": car.model,
                            "colour": car.colour,
                            "transmission": car.transmission,
                            "car_type": car.car_type,
                            "price": locale.currency(car.price, grouping= True),
                            "photo": os.path.join(app.config['UPLOAD_FOLDER'], car.photo),
                            "user_id": car.user_id
                        }

                    )
                return jsonify(cars),200
    except:
        return jsonify({"message": "Access token is missing or invalid"}),401

    return ''

@app.route('/api/users/<int:user_id>', methods=['GET'])
@login_required
def user(user_id):
    user_token= request.headers['Authorization'].split(' ')[1]
    if not user_token:
        return jsonify({"message": "Access token is missing or invalid"}),401
    try:
        decoded = jwt.decode(user_token, app.config['SECRET_KEY'], algorithms=['HS256'])
        if decoded['sub'] == current_user.username:
            if request.method == 'GET':
                returneduser = Users.query.filter_by(id=user_id).first()
                user = {
                    "id": returneduser.id,
                    "username": returneduser.username,
                    "name": returneduser.name,
                    "photo": returneduser.photo,
                    "email": returneduser.email,
                    "location": returneduser.location,
                    "biography": returneduser.biography,
                    "date_joined": returneduser.date_joined
                }
            return jsonify(user),200
    except:
        return jsonify({"message": "Access token is missing or invalid"}),401

@app.route('/api/users/<int:user_id>/favourites', methods=['GET'])
@login_required
def favourites(user_id):
    user_token= request.headers['Authorization'].split(' ')[1]
    if not user_token:
        return jsonify({"message": "Access token is missing or invalid"}),401
    try:
        decoded = jwt.decode(user_token, app.config['SECRET_KEY'], algorithms=['HS256'])
        if decoded['sub'] == current_user.username:
            if request.method == 'GET':
                returnedcars = []
                favourites = Favourites.query.filter_by(user_id=user_id).all()
                for favourite  in favourites:
                    tempcar = Cars.query.filter_by(id = favourite.car_id).first()
                    tempcarinfo={
                        "id": tempcar.id,
                        "description": tempcar.description,
                        "year": tempcar.year,
                        "make": tempcar.make,
                        "model": tempcar.model,
                        "colour": tempcar.colour,
                        "transmission": tempcar.transmission,
                        "car_type": tempcar.car_type,
                        "price": locale.currency(tempcar.price, grouping= True),
                        "photo": os.path.join(app.config['UPLOAD_FOLDER'], tempcar.photo)[1:],
                        "user_id": tempcar.user_id
                    }
                    if tempcarinfo in returnedcars:
                        continue
                    else:
                        returnedcars.append(tempcarinfo) 
                return jsonify(returnedcars),200
    except:
        return jsonify({"message": "Access token is missing or invalid"}),401

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.route('/api/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})

@app.route('/api/uid', methods=['GET'])
@login_required
def uid():
    user_token= request.headers['Authorization'].split(' ')[1]
    if not user_token:
         return jsonify({"message": "Access token is missing or invalid"}),401
    try:
        decoded = jwt.decode(user_token, app.config['SECRET_KEY'], algorithms=['HS256'])
        if decoded['sub'] == current_user.username:
            if request.method == "GET":
                return jsonify({"message": current_user.id}),200
    except:
        return jsonify({"message": "Access token is missing or invalid"}),401 

@app.route('/api/checkfavourite/<int:car_id>', methods= ['GET'])
@login_required
def checkfavourite(car_id):
    user_token= request.headers['Authorization'].split(' ')[1]
    if not user_token:
        return jsonify({"message": "Access token is missing or invalid"}),401
    try:
        decoded = jwt.decode(user_token, app.config['SECRET_KEY'], algorithms=['HS256'])
        if decoded['sub'] == current_user.username:
            if request.method == "GET":
                favourited= False
                current_favorites = Favourites.query.all()
                for fave in current_favorites:
                    if fave.user_id == current_user.id  and fave.car_id == car_id:
                        favourited = True
                if favourited:
                    return jsonify({"message": True}),200
                else:
                    return jsonify({"message": False}),200
    except:
        return jsonify({"message": False}),401

def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages


@app.route('/uploads/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return jsonify(error="Page Not Found"), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")