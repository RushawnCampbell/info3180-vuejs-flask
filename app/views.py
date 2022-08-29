from app import app, db, login_manager
from flask import request, jsonify, send_file, send_from_directory
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash

from app.models import Users, Personalinfo, Employerinfo, Kininfo
from app.forms import SigninForm, SigninForm


from flask_wtf.csrf import generate_csrf
import os, json, time, datetime, jwt, locale
import numpy as numpi

locale.setlocale( locale.LC_ALL, 'en_CA.UTF-8' )



@app.route('/')
def index():
    return send_file(os.path.join('../dist/', 'index.html'))


""" @app.route('/api/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        formobject =  SignupForm()
        if formobject.validate_on_submit():
            fileobj = request.files['photo']
            cleanedname = secure_filename(fileobj.filename)
            fileobj.save(os.path.join(app.config['UPLOAD_FOLDER'], cleanedname))
            if fileobj and (cleanedname != "" and cleanedname != " "):
                date_joined = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                newuser = Users(formobject.username.data,formobject.password.data, formobject.fullname.data, formobject.email.data,formobject.location.data, formobject.biography.data, cleanedname, date_joined )
                db.session.add(newuser)
                db.session.commit()
                userid =  db.session.query(Users.id).distinct().all()[-1][0]
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
"""
@app.route('/api/addata', methods=['GET'])
def addata():
    fileobj = open('/home/antidragon/Desktop/Python Dev/Skiptrace/uploads/data.json')
    data =  json.load(fileobj)
    count= 0
    for dobj in data:
        if count == 100:
            count = 0
            time.sleep(3)
        rec = Personalinfo(first_name = dobj['FIRST NAME'], last_name =  dobj['SURNAME'], middle_name =  dobj['MIDDLE NAME'], dob= dobj['DOB'], street_address=  dobj['ADDRESS'], city= dobj['CITY'], country= dobj['COUNTRY'])
        db.session.add(rec)
        db.session.commit()

    return jsonify({
        "message": "Success",
    }),200


@app.route('/api/auth/signin', methods=['POST'])
def signin():
    formobject = SigninForm()
    if request.method == "POST":
        if  formobject.validate_on_submit():
            username = formobject.username.data
            password =formobject.password.data
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

@app.route('/api/quicksearch', methods=['GET'])
@login_required
def quicksearch():
    user_token= request.headers['Authorization'].split(' ')[1]
    if not user_token:
        return jsonify({"message": "Access token is missing or invalid"}),401
    try:
        decoded = jwt.decode(user_token, app.config['SECRET_KEY'], algorithms=['HS256'])
        if decoded['sub'].lower() == current_user.username.lower():
        
            if request.method == 'GET':
                params = request.args

                quicksearch = params.get('quicksearchquery')
                if quicksearch == "" or quicksearch == " ":
                    return jsonify({"message":"You didn\'t search for anything."}),201

                queryarray = quicksearch.split(" ")
                resultantrecords= []
                searchedrecords =[]

                for entry in  queryarray:
                    tempsearch= Personalinfo.query.filter(Personalinfo.first_name == entry.lower() or Personalinfo.first_name == entry.upper()).distinct().all()
                    if tempsearch not in searchedrecords:
                        searchedrecords.append(tempsearch)

                    tempsearch= Personalinfo.query.filter(Personalinfo.middle_name == entry.lower() or Personalinfo.middle_name == entry.upper()).distinct().all()
                    if tempsearch not in searchedrecords:
                        searchedrecords.append(tempsearch)

                    tempsearch= Personalinfo.query.filter(Personalinfo.last_name == entry.lower() or Personalinfo.last_name == entry.upper()).distinct().all()
                    if tempsearch not in searchedrecords:
                        searchedrecords.append(tempsearch)

                    tempsearch= Personalinfo.query.filter(Personalinfo.nib == entry.lower() or Personalinfo.nib == entry.upper()).distinct().all()
                    if tempsearch not in searchedrecords:
                        searchedrecords.append(tempsearch)

                    tempsearch= Personalinfo.query.filter(Personalinfo.dob == entry.lower() or Personalinfo.dob == entry.upper()).distinct().all()
                    if tempsearch not in searchedrecords:
                        searchedrecords.append(tempsearch)

                    tempsearch= Personalinfo.query.filter(Personalinfo.gender == entry.lower() or Personalinfo.gender == entry.upper()).distinct().all()
                    if tempsearch not in searchedrecords:
                        searchedrecords.append(tempsearch)
                    tempsearch= Personalinfo.query.filter(Personalinfo.marital_status== entry.lower() or Personalinfo.marital_status == entry.upper()).distinct().all()
                    if tempsearch not in searchedrecords:
                        searchedrecords.append(tempsearch)

                    tempsearch= Personalinfo.query.filter(Personalinfo.home_phone == quicksearch).distinct().all()
                    if tempsearch not in searchedrecords:
                        searchedrecords.append(tempsearch)

                    tempsearch= Personalinfo.query.filter(Personalinfo.cell_phone == quicksearch).distinct().all()
                    if tempsearch not in searchedrecords:
                        searchedrecords.append(tempsearch)
                    tempsearch= Personalinfo.query.filter(Personalinfo.work_phone == quicksearch).distinct().all()
                    if tempsearch not in searchedrecords:
                        searchedrecords.append(tempsearch)
                    tempsearch= Personalinfo.query.filter(Personalinfo.street_address == quicksearch).distinct().all()
                    if tempsearch not in searchedrecords:
                        searchedrecords.append(tempsearch)
                    
                    tempsearch= Personalinfo.query.filter(Personalinfo.po_box == entry.lower() or Personalinfo.po_box == entry.upper()).distinct().all()
                    if tempsearch not in searchedrecords:
                        searchedrecords.append(tempsearch)
                    tempsearch= Personalinfo.query.filter(Personalinfo.city == entry.lower() or Personalinfo.city == entry.upper()).distinct().all()
                    if tempsearch not in searchedrecords:
                        searchedrecords.append(tempsearch)

                    tempsearch= Personalinfo.query.filter(Personalinfo.country == entry.lower() or Personalinfo.country == entry.upper()).distinct().all()
                    if tempsearch not in searchedrecords:
                        searchedrecords.append(tempsearch)

                if len(searchedrecords) == 0:
                    return jsonify({"message": "No Records Found"}),201 
                    
    
                for record in searchedrecords:
                    if len(record) == 0:
                            continue
                    for record in record:
                        resultantrecords.append({
                        "record_id": record.record_id,
                        "first_name" : record.first_name,
                        "middle_name" : record.middle_name,
                        "last_name" : record.last_name,
                        "nib": record.nib,
                        "dob": record.dob,
                        "gender": record.gender,
                        "marital_status": record.marital_status,
                        "home_phone": record.home_phone,
                        "cell_phone": record.cell_phone,
                        "work_phone": record.work_phone,
                        "street_address": record.street_address,
                        "po_box": record.po_box,
                        "city" : record.city,
                        "country": record.country
                    })
                return jsonify(resultantrecords),200
    except:
        return jsonify({"Something went wrong, tray again later."}),401

    return ''


@app.route('/api/advancesearch', methods=['GET'])
@login_required
def advancesearch():

    user_token= request.headers['Authorization'].split(' ')[1]
    if not user_token:
        return jsonify({"message": "Access token is missing or invalid"}),401
    try:
        decoded = jwt.decode(user_token, app.config['SECRET_KEY'], algorithms=['HS256'])
        resultantrecords= []
        searchedrecords = []
        tempsearch =[]
        if decoded['sub'].lower() == current_user.username.lower():
            if request.method == 'GET':
                params = []
                for arg, argval in request.args.items():
                    if argval == "" or argval == " " or argval is  None:
                        continue
                    else:
                        params.append((arg, argval))

                if len(params) == 0:
                    return jsonify({"message": "You didn't search for anything."}),201 


                if len(params) == 1:
                    for par in params:
                        if par[1] == "" or par[1]== " " or par[1] is  None:
                            return jsonify({"message": "You didn't search for anything."}),201 
                        else:
                            if par[0] == "firstname":
                                searchedrecords = Personalinfo.query.filter(Personalinfo.first_name == par[1].lower() ).distinct().all()
                            elif par[0] == "lastname":
                                searchedrecords = Personalinfo.query.filter(Personalinfo.last_name == par[1].lower() ).distinct().all()
                            
                           
                            if len(searchedrecords) == 0:
                                return jsonify({"message": "No Records Found"}),201 
                            else:
                                for record in searchedrecords:
                                    resultantrecords.append({
                                        "record_id": record.record_id,
                                        "first_name" : record.first_name,
                                        "middle_name" : record.middle_name,
                                        "last_name" : record.last_name,
                                        "nib": record.nib,
                                        "dob": record.dob,
                                        "gender": record.gender,
                                        "marital_status": record.marital_status,
                                        "home_phone": record.home_phone,
                                        "cell_phone": record.cell_phone,
                                        "work_phone": record.work_phone,
                                        "street_address": record.street_address,
                                        "po_box": record.po_box,
                                        "city" : record.city,
                                        "country": record.country
                                    })
                                return jsonify(resultantrecords),200



                for par in params:

                    if par[0] == "firstname":
                        tempsearch.append(Personalinfo.query.filter(Personalinfo.first_name == par[1].lower() ).distinct().all())
                        
                    if par[0] == "lastname":
                        tempsearch.append(Personalinfo.query.filter(Personalinfo.last_name == par[1].lower() ).distinct().all())

                    if par[0] == "dob":
                        tempsearch.append(Personalinfo.query.filter(Personalinfo.dob == par[1].lower() ).distinct().all())
                        

                    if par[0] == "nib":
                        tempsearch.append(Personalinfo.query.filter(Personalinfo.nib == par[1].lower() ).distinct().all())
                        
            
                if len(tempsearch)== 2:
                    searchedrecords = intersection(tempsearch[0], tempsearch[1]) 
                elif len(tempsearch) > 2:
                    searchedrecords = intersection(tempsearch[0], tempsearch[1]) 
                    for i in range(len(tempsearch)):
                        if i == 0 or i==1:
                            continue
                        searchedrecords = intersection(searchedrecords, tempsearch[i]) 
                
                
                if len(searchedrecords) == 0:
                    return jsonify({"message": "No Records Found"}),201 
                        

                for record in searchedrecords:
                    resultantrecords.append({
                        "record_id": record.record_id,
                        "first_name" : record.first_name,
                        "middle_name" : record.middle_name,
                        "last_name" : record.last_name,
                        "nib": record.nib,
                        "dob": record.dob,
                        "gender": record.gender,
                        "marital_status": record.marital_status,
                        "home_phone": record.home_phone,
                        "cell_phone": record.cell_phone,
                        "work_phone": record.work_phone,
                        "street_address": record.street_address,
                        "po_box": record.po_box,
                        "city" : record.city,
                        "country": record.country
                    })
                
    
                return jsonify(resultantrecords),200
    except:
        return jsonify({"Something went wrong, tray again later."}),401

    return ''

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

@app.route('/api/auth/signout', methods=['GET'])
@login_required
def signout():
        if request.method == 'GET':
            logout_user()
            return jsonify({
                "message": "Log out successful"
            }),200

@login_manager.user_loader
def load_user(id):
    return Users.query.get(id)


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