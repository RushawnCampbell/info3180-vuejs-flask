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
        searchedrecords =[]
        tempsearch=[]
        emptycounter=0
        if decoded['sub'].lower() == current_user.username.lower():
            if request.method == 'GET':
                params = request.args
                
                for par, parval in params.items():
                    if par == "firstname":
                        if parval == "" or parval == " " or parval is  None:
                            emptycounter+=1
                            continue
                        elif len(tempsearch) == 0:
                            tempsearch= Personalinfo.query.filter(Personalinfo.first_name == parval.lower() ).distinct().all()
                            for rec in tempsearch:
                                searchedrecords.append(rec)
                            continue
                        else:
                            for rec in searchedrecords:
                                if rec.first_name == parval.lower() or rec.first_name == parval.upper():
                                    searchedrecords.clear()
                                    searchedrecords.append(rec)

                                     
                    
                    if par == "lastname":
                        if parval == "" or parval == " " or parval is  None:
                            emptycounter+=1
                            continue
                        elif len(tempsearch) == 0:
                            tempsearch= Personalinfo.query.filter(Personalinfo.last_name == parval.lower() ).distinct().all()
                            for rec in tempsearch:
                                searchedrecords.append(rec)
                            continue
                        else:
                            for rec in searchedrecords:
                                if rec.last_name == parval.lower() or rec.last_name == parval.upper():
                                    searchedrecords.clear()
                                    searchedrecords.append(rec)
                       

                    if par == "dob":
                        if parval == "" or parval == " " or parval is  None:
                            emptycounter+=1
                            continue
                        elif len(tempsearch) == 0:
                            tempsearch= Personalinfo.query.filter(Personalinfo.dob == parval.lower() ).distinct().all()
                            for rec in tempsearch:
                                searchedrecords.append(rec)
                            continue
                        else:
                            for rec in searchedrecords:
                                if rec.dob == parval.lower() or rec.dob == parval.upper():
                                    searchedrecords.clear()
                                    searchedrecords.append(rec)
                    

                    if par == "nib":
                        if parval == "" or parval == " " or parval is  None:
                            emptycounter+=1
                            continue
                        elif len(tempsearch) == 0:
                            tempsearch= Personalinfo.query.filter(Personalinfo.nib == parval.lower() ).distinct().all()
                            for rec in tempsearch:
                                searchedrecords.append(rec)
                            continue
                        else:
                            for rec in searchedrecords:
                                if rec.nib == parval.lower() or rec.nib == parval.upper():
                                    searchedrecords.clear()
                                    searchedrecords.append(rec)
                        
                   
                if emptycounter == len(params):
                    return jsonify({"message": "You didn't search for anything."}),201 

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





    for (let rec=0; rec<records.length; rec++){
                            const recorditem = document.createElement("div");
                            recorditem.setAttribute('id', 'recorditem');
                                        
                            const recordimg = document.createElement('img');
                            recordimg.setAttribute('src', 'src/assets/images/user.png' );
                            recordimg.setAttribute('class', 'recorditem' );

                            const fnamespanlabel = document.createElement('span');
                            fnamespanlabel.setAttribute('class', 'fieldtitle');
                            fnamespanlabel.appendChild(document.createTextNode('First Name'));

                            const lnamespanlabel = document.createElement('span');
                            lnamespanlabel.setAttribute('class', 'fieldtitle');
                            lnamespanlabel.appendChild(document.createTextNode('Last Name'));

                            const dobspanlabel = document.createElement('span');
                            dobspanlabel.setAttribute('class', 'fieldtitle');
                            dobspanlabel.appendChild(document.createTextNode('D.O.B'));

                            const nibspanlabel = document.createElement('span');
                            nibspanlabel.setAttribute('class', 'fieldtitle');
                            nibspanlabel.appendChild(document.createTextNode('NIB#'));

                            const homepspanlabel = document.createElement('span');
                            homepspanlabel.setAttribute('class', 'fieldtitle');
                            homepspanlabel.appendChild(document.createTextNode('Home Phone'));

                            const cellpspanlabel = document.createElement('span');
                            cellpspanlabel.setAttribute('class', 'fieldtitle');
                            cellpspanlabel.appendChild(document.createTextNode('Cell Phone'));

                            const workpspanlabel = document.createElement('span');
                            workpspanlabel.setAttribute('class', 'fieldtitle');
                            workpspanlabel.appendChild(document.createTextNode('Work Phone'));

                            const saddressspanlabel = document.createElement('span');
                            saddressspanlabel.setAttribute('class', 'fieldtitle');
                            saddressspanlabel.appendChild(document.createTextNode('Street Address'));

                            const cityspanlabel = document.createElement('span');
                            cityspanlabel.setAttribute('class', 'fieldtitle');
                            cityspanlabel.appendChild(document.createTextNode('City'));
                            
                            const fnameinfo = document.createElement('div');
                            fnameinfo.setAttribute('class', 'rowinfo');
                            const fnamespanvalue= document.createElement('span');
                            fnamespanvalue.appendChild(document.createTextNode(records[rec].first_name));
                            fnameinfo.appendChild(fnamespanlabel);
                            fnameinfo.appendChild(fnamespanvalue);


                            const lnameinfo = document.createElement('div');
                            lnameinfo.setAttribute('class', 'rowinfo');
                            const lnamespanvalue= document.createElement('span');
                            lnamespanvalue.appendChild(document.createTextNode(records[rec].last_name));
                            lnameinfo.appendChild(lnamespanlabel);
                            lnameinfo.appendChild(lnamespanvalue);


                            const dobinfo = document.createElement('div');
                            dobinfo.setAttribute('class', 'rowinfo');
                            const dobspanvalue= document.createElement('span');
                            dobspanvalue.appendChild(document.createTextNode(records[rec].dob));
                            dobinfo.appendChild(dobspanlabel);
                            dobinfo.appendChild(dobspanvalue);


                            const nibinfo = document.createElement('div');
                            nibinfo.setAttribute('class', 'rowinfo');
                            const nibspanvalue= document.createElement('span');
                            nibspanvalue.appendChild(document.createTextNode(records[rec].nib));
                            nibinfo.appendChild(nibspanlabel);
                            nibinfo.appendChild(nibspanvalue);


                            const homepinfo = document.createElement('div');
                            homepinfo.setAttribute('class', 'rowinfo');
                            const homepspanvalue= document.createElement('span');
                            homepspanvalue.appendChild(document.createTextNode(records[rec].home_phone));
                            homepinfo.appendChild(homepspanlabel);
                            homepinfo.appendChild(homepspanvalue);


                            const cellpinfo = document.createElement('div');
                            cellpinfo.setAttribute('class', 'rowinfo');
                            const cellpspanvalue= document.createElement('span');
                            cellpspanvalue.appendChild(document.createTextNode(records[rec].cell_phone));
                            cellpinfo.appendChild(cellpspanlabel);
                            cellpinfo.appendChild(cellpspanvalue);

                            const workpinfo = document.createElement('div');
                            workpinfo.setAttribute('class', 'rowinfo');
                            const workpspanvalue= document.createElement('span');
                            workpspanvalue.appendChild(document.createTextNode(records[rec].work_phone));
                            workpinfo.appendChild(workpspanlabel);
                            workpinfo.appendChild(workpspanvalue);



                            const saddressinfo = document.createElement('div');
                            saddressinfo.setAttribute('class', 'rowinfo');
                            const saddressspanvalue= document.createElement('span');
                            saddressspanvalue.appendChild(document.createTextNode(records[rec].street_address));
                            saddressinfo.appendChild(saddressspanlabel);
                            saddressinfo.appendChild(saddressspanvalue);


                            const cityinfo = document.createElement('div');
                            cityinfo.setAttribute('class', 'rowinfo');
                            const cityspanvalue= document.createElement('span');
                            cityspanvalue.appendChild(document.createTextNode(records[rec].city));
                            cityinfo.appendChild(cityspanlabel);
                            cityinfo.appendChild(cityspanvalue);


                            const moreinfo =document.createElement('a');
                            moreinfo.setAttribute('class', 'btn');
                            moreinfo.classList.add('btnsignin');
                            moreinfo.innerHTML = "MORE INFO";

                            moreinfo.addEventListener("click",function (){
                                sessionStorage.setItem('issingle', true);
                                this.issingle =true;
                                sessionStorage.setItem('isresult', false);
                                this.isresult = false;
                                const msg = document.querySelector("section#msg");
                                msg.classList.add('hide');
                                msg.classList.remove('show');

                                const pagination =  document.querySelector("div#pagination");


                                pagination.classList.remove("showgrid");
                                pagination.classList.add("hidecontainer");

                                let itemchecker =setInterval(()=>{
                                    if(document.contains(document.querySelector('h2#firstname'))){
                        
                                        document.querySelector('h2#firstname').innerHTML ='';
                                        document.querySelector('h2#firstname').appendChild(document.createTextNode(records[rec].first_name));

                                        document.querySelector('h2#lastname').innerHTML = '';
                                        document.querySelector('h2#lastname').appendChild(document.createTextNode(records[rec].last_name));

                                        document.querySelector('span#inforowmiddle').innerHTML;
                                        document.querySelector('span#inforowmiddle').appendChild(document.createTextNode(records[rec].middle_name));

                                        document.querySelector('span#inforownib').innerHTML ='';
                                        document.querySelector('span#inforownib').appendChild(document.createTextNode(records[rec].nib));

                                        document.querySelector('span#inforowdob').innerHTML= '';
                                        document.querySelector('span#inforowdob').appendChild(document.createTextNode(records[rec].dob));

                                        document.querySelector('span#inforowgender').innerHTML = '';
                                        document.querySelector('span#inforowgender').appendChild(document.createTextNode(records[rec].gender));

                                        document.querySelector('span#inforowmar').innerHTML = '';
                                        document.querySelector('span#inforowmar').appendChild(document.createTextNode(records[rec].marital_status));

                                        document.querySelector('span#inforowhphone').innerHTML= '';
                                        document.querySelector('span#inforowhphone').appendChild(document.createTextNode(records[rec].home_phone));
                                        
                                        document.querySelector('span#inforowcphone').innerHTML = '';
                                        document.querySelector('span#inforowcphone').appendChild(document.createTextNode(records[rec].cell_phone));

                                        document.querySelector('span#inforowwphone').innerHTML = '';
                                        document.querySelector('span#inforowwphone').appendChild(document.createTextNode(records[rec].work_phone));

                                        document.querySelector('span#inforowsaddress').innerHTML = '';
                                        document.querySelector('span#inforowsaddress').appendChild(document.createTextNode(records[rec].street_address));

                                        document.querySelector('span#inforowcity').innerHTML ='';
                                        document.querySelector('span#inforowcity').appendChild(document.createTextNode(records[rec].city));

                                        document.querySelector('span#inforowcountry').innerHTML = '';
                                        document.querySelector('span#inforowcountry').appendChild(document.createTextNode(records[rec].country));


                                        document.querySelector("button#backresults").addEventListener('click', ()=>{
                                            sessionStorage.setItem('issingle', false);
                                            this.issingle =false;
                                            sessionStorage.setItem('isresult', true);
                                            this.isresult = true;
                                            msg.classList.remove('hide');
                                            msg.classList.add('show');
                                            pagination.classList.add("showgrid");
                                            pagination.classList.remove("hidecontainer");

                                            let pagebtns = document.querySelectorAll("div#pagination button");

                                            let backchecker =  setInterval(()=>{

if (document.contains(document.querySelector("section.resultcontainer"))){
    clearInterval(backchecker);
    document.querySelector("section.resultcontainer").innerHTML = "";
    pagebtns.forEach((btn)=>{
    
        btn.addEventListener('click',()=>{
            
            document.querySelector("section.resultcontainer").innerHTML = "";
            let records = vanillarecords.slice( ( parseInt(btn.getAttribute('id')) * pagelim) - (pagelim), (parseInt(btn.getAttribute('id')) * pagelim));      
            for (let rec=0; rec<records.length; rec++){
            const recorditem = document.createElement("div");
            recorditem.setAttribute('id', 'recorditem');
                        
            const recordimg = document.createElement('img');
            recordimg.setAttribute('src', 'src/assets/images/user.png' );
            recordimg.setAttribute('class', 'recorditem' );

            const fnamespanlabel = document.createElement('span');
            fnamespanlabel.setAttribute('class', 'fieldtitle');
            fnamespanlabel.appendChild(document.createTextNode('First Name'));

            const lnamespanlabel = document.createElement('span');
            lnamespanlabel.setAttribute('class', 'fieldtitle');
            lnamespanlabel.appendChild(document.createTextNode('Last Name'));

            const dobspanlabel = document.createElement('span');
            dobspanlabel.setAttribute('class', 'fieldtitle');
            dobspanlabel.appendChild(document.createTextNode('D.O.B'));

            const nibspanlabel = document.createElement('span');
            nibspanlabel.setAttribute('class', 'fieldtitle');
            nibspanlabel.appendChild(document.createTextNode('NIB#'));

            const homepspanlabel = document.createElement('span');
            homepspanlabel.setAttribute('class', 'fieldtitle');
            homepspanlabel.appendChild(document.createTextNode('Home Phone'));

            const cellpspanlabel = document.createElement('span');
            cellpspanlabel.setAttribute('class', 'fieldtitle');
            cellpspanlabel.appendChild(document.createTextNode('Cell Phone'));

            const workpspanlabel = document.createElement('span');
            workpspanlabel.setAttribute('class', 'fieldtitle');
            workpspanlabel.appendChild(document.createTextNode('Work Phone'));

            const saddressspanlabel = document.createElement('span');
            saddressspanlabel.setAttribute('class', 'fieldtitle');
            saddressspanlabel.appendChild(document.createTextNode('Street Address'));

            const cityspanlabel = document.createElement('span');
            cityspanlabel.setAttribute('class', 'fieldtitle');
            cityspanlabel.appendChild(document.createTextNode('City'));

            const fnameinfo = document.createElement('div');
            fnameinfo.setAttribute('class', 'rowinfo');
            const fnamespanvalue= document.createElement('span');
            fnamespanvalue.appendChild(document.createTextNode(records[rec].first_name));
            fnameinfo.appendChild(fnamespanlabel);
            fnameinfo.appendChild(fnamespanvalue);


            const lnameinfo = document.createElement('div');
            lnameinfo.setAttribute('class', 'rowinfo');
            const lnamespanvalue= document.createElement('span');
            lnamespanvalue.appendChild(document.createTextNode(records[rec].last_name));
            lnameinfo.appendChild(lnamespanlabel);
            lnameinfo.appendChild(lnamespanvalue);


            const dobinfo = document.createElement('div');
            dobinfo.setAttribute('class', 'rowinfo');
            const dobspanvalue= document.createElement('span');
            dobspanvalue.appendChild(document.createTextNode(records[rec].dob));
            dobinfo.appendChild(dobspanlabel);
            dobinfo.appendChild(dobspanvalue);


            const nibinfo = document.createElement('div');
            nibinfo.setAttribute('class', 'rowinfo');
            const nibspanvalue= document.createElement('span');
            nibspanvalue.appendChild(document.createTextNode(records[rec].nib));
            nibinfo.appendChild(nibspanlabel);
            nibinfo.appendChild(nibspanvalue);


            const homepinfo = document.createElement('div');
            homepinfo.setAttribute('class', 'rowinfo');
            const homepspanvalue= document.createElement('span');
            homepspanvalue.appendChild(document.createTextNode(records[rec].home_phone));
            homepinfo.appendChild(homepspanlabel);
            homepinfo.appendChild(homepspanvalue);


            const cellpinfo = document.createElement('div');
            cellpinfo.setAttribute('class', 'rowinfo');
            const cellpspanvalue= document.createElement('span');
            cellpspanvalue.appendChild(document.createTextNode(records[rec].cell_phone));
            cellpinfo.appendChild(cellpspanlabel);
            cellpinfo.appendChild(cellpspanvalue);

            const workpinfo = document.createElement('div');
            workpinfo.setAttribute('class', 'rowinfo');
            const workpspanvalue= document.createElement('span');
            workpspanvalue.appendChild(document.createTextNode(records[rec].work_phone));
            workpinfo.appendChild(workpspanlabel);
            workpinfo.appendChild(workpspanvalue);



            const saddressinfo = document.createElement('div');
            saddressinfo.setAttribute('class', 'rowinfo');
            const saddressspanvalue= document.createElement('span');
            saddressspanvalue.appendChild(document.createTextNode(records[rec].street_address));
            saddressinfo.appendChild(saddressspanlabel);
            saddressinfo.appendChild(saddressspanvalue);


            const cityinfo = document.createElement('div');
            cityinfo.setAttribute('class', 'rowinfo');
            const cityspanvalue= document.createElement('span');
            cityspanvalue.appendChild(document.createTextNode(records[rec].city));
            cityinfo.appendChild(cityspanlabel);
            cityinfo.appendChild(cityspanvalue);


            const moreinfo =document.createElement('a');
            moreinfo.setAttribute('class', 'btn');
            moreinfo.classList.add('btnsignin');
            moreinfo.innerHTML = "MORE INFO";

            moreinfo.addEventListener("click",function (){
                sessionStorage.setItem('issingle', true);
                this.issingle =true;
                sessionStorage.setItem('isresult', false);
                this.isresult = false;
                const msg = document.querySelector("section#msg");
                msg.classList.add('hide');
                msg.classList.remove('show');

                const pagination =  document.querySelector("div#pagination");


                pagination.classList.remove("showgrid");
                pagination.classList.add("hidecontainer");

                let itemchecker =setInterval(()=>{
                    if(document.contains(document.querySelector('h2#firstname'))){
        
                        document.querySelector('h2#firstname').innerHTML ='';
                        document.querySelector('h2#firstname').appendChild(document.createTextNode(records[rec].first_name));

                        document.querySelector('h2#lastname').innerHTML = '';
                        document.querySelector('h2#lastname').appendChild(document.createTextNode(records[rec].last_name));

                        document.querySelector('span#inforowmiddle').innerHTML;
                        document.querySelector('span#inforowmiddle').appendChild(document.createTextNode(records[rec].middle_name));

                        document.querySelector('span#inforownib').innerHTML ='';
                        document.querySelector('span#inforownib').appendChild(document.createTextNode(records[rec].nib));

                        document.querySelector('span#inforowdob').innerHTML= '';
                        document.querySelector('span#inforowdob').appendChild(document.createTextNode(records[rec].dob));

                        document.querySelector('span#inforowgender').innerHTML = '';
                        document.querySelector('span#inforowgender').appendChild(document.createTextNode(records[rec].gender));

                        document.querySelector('span#inforowmar').innerHTML = '';
                        document.querySelector('span#inforowmar').appendChild(document.createTextNode(records[rec].marital_status));

                        document.querySelector('span#inforowhphone').innerHTML= '';
                        document.querySelector('span#inforowhphone').appendChild(document.createTextNode(records[rec].home_phone));
                        
                        document.querySelector('span#inforowcphone').innerHTML = '';
                        document.querySelector('span#inforowcphone').appendChild(document.createTextNode(records[rec].cell_phone));

                        document.querySelector('span#inforowwphone').innerHTML = '';
                        document.querySelector('span#inforowwphone').appendChild(document.createTextNode(records[rec].work_phone));

                        document.querySelector('span#inforowsaddress').innerHTML = '';
                        document.querySelector('span#inforowsaddress').appendChild(document.createTextNode(records[rec].street_address));

                        document.querySelector('span#inforowcity').innerHTML ='';
                        document.querySelector('span#inforowcity').appendChild(document.createTextNode(records[rec].city));

                        document.querySelector('span#inforowcountry').innerHTML = '';
                        document.querySelector('span#inforowcountry').appendChild(document.createTextNode(records[rec].country));


                        document.querySelector("button#backresults").addEventListener('click', ()=>{
                            sessionStorage.setItem('issingle', false);
                            this.issingle =false;
                            sessionStorage.setItem('isresult', true);
                            this.isresult = true;
                            msg.classList.remove('hide');
                            msg.classList.add('show');
                            pagination.classList.add("showgrid");
                            pagination.classList.remove("hidecontainer");

                            let pagebtns = document.querySelectorAll("div#pagination button");


let backchecker =  setInterval(()=>{

if (document.contains(document.querySelector("section.resultcontainer"))){
clearInterval(backchecker);
document.querySelector("section.resultcontainer").innerHTML = "";
pagebtns.forEach((btn)=>{

btn.addEventListener('click',()=>{
document.querySelector("section.resultcontainer").innerHTML = "";
let records = vanillarecords.slice( ( parseInt(btn.getAttribute('id')) * pagelim) - (pagelim), (parseInt(btn.getAttribute('id')) * pagelim));      
for (let rec=0; rec<records.length; rec++){
const recorditem = document.createElement("div");
recorditem.setAttribute('id', 'recorditem');

const recordimg = document.createElement('img');
recordimg.setAttribute('src', 'src/assets/images/user.png' );
recordimg.setAttribute('class', 'recorditem' );

const fnamespanlabel = document.createElement('span');
fnamespanlabel.setAttribute('class', 'fieldtitle');
fnamespanlabel.appendChild(document.createTextNode('First Name'));

const lnamespanlabel = document.createElement('span');
lnamespanlabel.setAttribute('class', 'fieldtitle');
lnamespanlabel.appendChild(document.createTextNode('Last Name'));

const dobspanlabel = document.createElement('span');
dobspanlabel.setAttribute('class', 'fieldtitle');
dobspanlabel.appendChild(document.createTextNode('D.O.B'));

const nibspanlabel = document.createElement('span');
nibspanlabel.setAttribute('class', 'fieldtitle');
nibspanlabel.appendChild(document.createTextNode('NIB#'));

const homepspanlabel = document.createElement('span');
homepspanlabel.setAttribute('class', 'fieldtitle');
homepspanlabel.appendChild(document.createTextNode('Home Phone'));

const cellpspanlabel = document.createElement('span');
cellpspanlabel.setAttribute('class', 'fieldtitle');
cellpspanlabel.appendChild(document.createTextNode('Cell Phone'));

const workpspanlabel = document.createElement('span');
workpspanlabel.setAttribute('class', 'fieldtitle');
workpspanlabel.appendChild(document.createTextNode('Work Phone'));

const saddressspanlabel = document.createElement('span');
saddressspanlabel.setAttribute('class', 'fieldtitle');
saddressspanlabel.appendChild(document.createTextNode('Street Address'));

const cityspanlabel = document.createElement('span');
cityspanlabel.setAttribute('class', 'fieldtitle');
cityspanlabel.appendChild(document.createTextNode('City'));

const fnameinfo = document.createElement('div');
fnameinfo.setAttribute('class', 'rowinfo');
const fnamespanvalue= document.createElement('span');
fnamespanvalue.appendChild(document.createTextNode(records[rec].first_name));
fnameinfo.appendChild(fnamespanlabel);
fnameinfo.appendChild(fnamespanvalue);


const lnameinfo = document.createElement('div');
lnameinfo.setAttribute('class', 'rowinfo');
const lnamespanvalue= document.createElement('span');
lnamespanvalue.appendChild(document.createTextNode(records[rec].last_name));
lnameinfo.appendChild(lnamespanlabel);
lnameinfo.appendChild(lnamespanvalue);


const dobinfo = document.createElement('div');
dobinfo.setAttribute('class', 'rowinfo');
const dobspanvalue= document.createElement('span');
dobspanvalue.appendChild(document.createTextNode(records[rec].dob));
dobinfo.appendChild(dobspanlabel);
dobinfo.appendChild(dobspanvalue);


const nibinfo = document.createElement('div');
nibinfo.setAttribute('class', 'rowinfo');
const nibspanvalue= document.createElement('span');
nibspanvalue.appendChild(document.createTextNode(records[rec].nib));
nibinfo.appendChild(nibspanlabel);
nibinfo.appendChild(nibspanvalue);


const homepinfo = document.createElement('div');
homepinfo.setAttribute('class', 'rowinfo');
const homepspanvalue= document.createElement('span');
homepspanvalue.appendChild(document.createTextNode(records[rec].home_phone));
homepinfo.appendChild(homepspanlabel);
homepinfo.appendChild(homepspanvalue);


const cellpinfo = document.createElement('div');
cellpinfo.setAttribute('class', 'rowinfo');
const cellpspanvalue= document.createElement('span');
cellpspanvalue.appendChild(document.createTextNode(records[rec].cell_phone));
cellpinfo.appendChild(cellpspanlabel);
cellpinfo.appendChild(cellpspanvalue);

const workpinfo = document.createElement('div');
workpinfo.setAttribute('class', 'rowinfo');
const workpspanvalue= document.createElement('span');
workpspanvalue.appendChild(document.createTextNode(records[rec].work_phone));
workpinfo.appendChild(workpspanlabel);
workpinfo.appendChild(workpspanvalue);



const saddressinfo = document.createElement('div');
saddressinfo.setAttribute('class', 'rowinfo');
const saddressspanvalue= document.createElement('span');
saddressspanvalue.appendChild(document.createTextNode(records[rec].street_address));
saddressinfo.appendChild(saddressspanlabel);
saddressinfo.appendChild(saddressspanvalue);


const cityinfo = document.createElement('div');
cityinfo.setAttribute('class', 'rowinfo');
const cityspanvalue= document.createElement('span');
cityspanvalue.appendChild(document.createTextNode(records[rec].city));
cityinfo.appendChild(cityspanlabel);
cityinfo.appendChild(cityspanvalue);


const moreinfo =document.createElement('a');
moreinfo.setAttribute('class', 'btn');
moreinfo.classList.add('btnsignin');
moreinfo.innerHTML = "MORE INFO";

moreinfo.addEventListener("click",function (){
sessionStorage.setItem('issingle', true);
this.issingle =true;
sessionStorage.setItem('isresult', false);
this.isresult = false;
const msg = document.querySelector("section#msg");
msg.classList.add('hide');
msg.classList.remove('show');

const pagination =  document.querySelector("div#pagination");


pagination.classList.remove("showgrid");
pagination.classList.add("hidecontainer");

let itemchecker =setInterval(()=>{
if(document.contains(document.querySelector('h2#firstname'))){

document.querySelector('h2#firstname').innerHTML ='';
document.querySelector('h2#firstname').appendChild(document.createTextNode(records[rec].first_name));

document.querySelector('h2#lastname').innerHTML = '';
document.querySelector('h2#lastname').appendChild(document.createTextNode(records[rec].last_name));

document.querySelector('span#inforowmiddle').innerHTML;
document.querySelector('span#inforowmiddle').appendChild(document.createTextNode(records[rec].middle_name));

document.querySelector('span#inforownib').innerHTML ='';
document.querySelector('span#inforownib').appendChild(document.createTextNode(records[rec].nib));

document.querySelector('span#inforowdob').innerHTML= '';
document.querySelector('span#inforowdob').appendChild(document.createTextNode(records[rec].dob));

document.querySelector('span#inforowgender').innerHTML = '';
document.querySelector('span#inforowgender').appendChild(document.createTextNode(records[rec].gender));

document.querySelector('span#inforowmar').innerHTML = '';
document.querySelector('span#inforowmar').appendChild(document.createTextNode(records[rec].marital_status));

document.querySelector('span#inforowhphone').innerHTML= '';
document.querySelector('span#inforowhphone').appendChild(document.createTextNode(records[rec].home_phone));

document.querySelector('span#inforowcphone').innerHTML = '';
document.querySelector('span#inforowcphone').appendChild(document.createTextNode(records[rec].cell_phone));

document.querySelector('span#inforowwphone').innerHTML = '';
document.querySelector('span#inforowwphone').appendChild(document.createTextNode(records[rec].work_phone));

document.querySelector('span#inforowsaddress').innerHTML = '';
document.querySelector('span#inforowsaddress').appendChild(document.createTextNode(records[rec].street_address));

document.querySelector('span#inforowcity').innerHTML ='';
document.querySelector('span#inforowcity').appendChild(document.createTextNode(records[rec].city));

document.querySelector('span#inforowcountry').innerHTML = '';
document.querySelector('span#inforowcountry').appendChild(document.createTextNode(records[rec].country));


document.querySelector("button#backresults").addEventListener('click', ()=>{
sessionStorage.setItem('issingle', false);
this.issingle =false;
sessionStorage.setItem('isresult', true);
this.isresult = true;
msg.classList.remove('hide');
msg.classList.add('show');
pagination.classList.add("showgrid");
pagination.classList.remove("hidecontainer");

let pagebtns = document.querySelectorAll("div#pagination button");

});

clearInterval(itemchecker);
}

}, 1);

});


recorditem.appendChild(recordimg);
recorditem.appendChild(fnameinfo);
recorditem.appendChild(lnameinfo);
recorditem.appendChild(dobinfo);
recorditem.appendChild(nibinfo);
recorditem.appendChild(homepinfo);
recorditem.appendChild(cellpinfo);
recorditem.appendChild(workpinfo);
recorditem.appendChild(saddressinfo);
recorditem.appendChild(cityinfo);
recorditem.appendChild(moreinfo);

document.querySelector("section.resultcontainer").appendChild(recorditem);


}

});


});

}

},0);
                        
                        });

                        clearInterval(itemchecker);
                    }

                }, 1);
                
            });


            recorditem.appendChild(recordimg);
            recorditem.appendChild(fnameinfo);
            recorditem.appendChild(lnameinfo);
            recorditem.appendChild(dobinfo);
            recorditem.appendChild(nibinfo);
            recorditem.appendChild(homepinfo);
            recorditem.appendChild(cellpinfo);
            recorditem.appendChild(workpinfo);
            recorditem.appendChild(saddressinfo);
            recorditem.appendChild(cityinfo);
            recorditem.appendChild(moreinfo);

            document.querySelector("section.resultcontainer").appendChild(recorditem);


    }

        });
    
        
});

}

},0);
                                        
                                        });

                                        clearInterval(itemchecker);
                                    }

                                }, 0);
                                
                            });


                            recorditem.appendChild(recordimg);
                            recorditem.appendChild(fnameinfo);
                            recorditem.appendChild(lnameinfo);
                            recorditem.appendChild(dobinfo);
                            recorditem.appendChild(nibinfo);
                            recorditem.appendChild(homepinfo);
                            recorditem.appendChild(cellpinfo);
                            recorditem.appendChild(workpinfo);
                            recorditem.appendChild(saddressinfo);
                            recorditem.appendChild(cityinfo);
                            recorditem.appendChild(moreinfo);

                           document.querySelector("section.resultcontainer").appendChild(recorditem);


                    }