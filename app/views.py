"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db, login_manager
from flask import request, session,jsonify, send_file
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
import json
import datetime 
import jwt


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


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
                userid =  userid = db.session.query(Users.id).all()[-1][0]
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
        return jsonify(form_errors(formobject))  

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
                   
    return ''

@app.route('/api/auth/logout', methods=['POST'])
@login_required
def logout():
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
        return jsonify({'message': 'No token provided, this request is illegal.'})
    try:
        decoded = jwt.decode(user_token, app.config['SECRET_KEY'], algorithms=['HS256'])
        if decoded['sub'] == current_user.username:
            cars = []
            returnedcars = Cars.query.all()
            for car in returnedcars:
                cars.push({
                    "id": car.id,
                    "description": car.description,
                    "year": car.year,
                    "make": car.make,
                    "model": car.model,
                    "colour": car.colour,
                    "transmission": car.transmission,
                    "car_type": car.car_type,
                    "price": car.price,
                    "photo": car.photo,
                    "user_id": car.user_id
                })
            cars = [cars[-3], cars[-2], cars[-1]]
            print(cars)
            #cars.push(db.session.filter.all()[-2])
            #cars.push(db.session.filter.all()[-1])
            return jsonify({'message': 'Hello'})
    except:
        return jsonify({'message': 'Invalid token provided'})

@app.route('/api/cars/{car_id}', methods=['GET'])
@login_required
def singlecar(car_id):
    return ''

@app.route('/api/cars/{car_id}/favourite', methods=['POST'])
@login_required
def favourite(car_id):
    return ''

@app.route('/api/search', methods=['GET'])
@login_required
def search():
    return ''

@app.route('/api/users/{user_id}', methods=['GET'])
@login_required
def user(user_id):
    return ''

@app.route('/api/users/{user_id}/favourites', methods=['GET'])
@login_required
def favourites(user_id):
    return ''

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

@app.route('/api/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})


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