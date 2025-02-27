from . import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash



class Personalinfo(db.Model):
    __tablename__='personalinfo'

    record_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name= db.Column(db.String(255))
    middle_name = db.Column(db.String(255),nullable=True, default=None)
    last_name= db.Column(db.String(255))
    nib =db.Column(db.String(55),nullable=True, default=None)
    dob= db.Column(db.Date,nullable=True, default=None)
    gender= db.Column(db.String(25))
    marital_status= db.Column(db.String(25))
    home_phone= db.Column(db.String(12))
    cell_phone = db.Column(db.String(12))
    work_phone = db.Column(db.String(12))
    street_address= db.Column(db.Text,)
    po_box = db.Column(db.String(55))
    city= db.Column(db.String(255))
    country= db.Column(db.String(255))
    employerinfo = relationship("Employerinfo", backref="employerinfo")
    kininfo =  relationship ("Kininfo", backref="kininfo")

    def __init__(self,first_name, last_name, middle_name, nib=None, dob=None, gender=None, marital_status=None, home_phone=None,cell_phone=None, work_phone=None, street_address=None, po_box=None, city=None, country=None):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.nib = nib
        self.dob = dob
        self.gender = gender
        self.marital_status = marital_status
        self.home_phone = home_phone
        self.cell_phone = cell_phone
        self.work_phone = work_phone
        self.street_address = street_address
        self.po_box = po_box
        self.city = city
        self.country = country

        

class Employerinfo (db.Model):
    __tablename__='employerinfo'

    record_id = db.Column(db.Integer, ForeignKey('personalinfo.record_id'), primary_key=True)
    first_name= db.Column(db.String(255))
    middle_name = db.Column(db.String(255))
    last_name= db.Column(db.String(255))
    phone= db.Column(db.String(255))
    street_address= db.Column(db.Text)
    po_box = db.Column(db.String(55))
    city= db.Column(db.String(255))
    country= db.Column(db.Text)

    def __init__(self,record_id, first_name=None, middle_name=None, last_name=None,phone=None, street_address=None, po_box=None, city=None, country=None ):
        
        self.record_id = record_id
        self.first_name= first_name
        self.middle_name = middle_name
        self.last_name= last_name
        self.phone= phone
        self.street_address= street_address
        self.po_box = po_box
        self.city = city
        self.country = country


class Kininfo(db.Model):

    __tablename__='kininfo'

    record_id = db.Column(db.Integer, ForeignKey('personalinfo.record_id'), primary_key=True)
    first_name= db.Column(db.String(255))
    middle_name = db.Column(db.String(255))
    last_name= db.Column(db.String(255))
    home_phone= db.Column(db.String(12))
    street_address= db.Column(db.String(255))
    city= db.Column(db.String(255))
    country= db.Column(db.String(255))
    employer_name= db.Column(db.String(255))
    employer_phone= db.Column(db.String(255))
    employer_street_address= db.Column(db.Text)
    employer_po_box = db.Column(db.String(55))
    employer_city= db.Column(db.String(255))
    employer_country= db.Column(db.Text)
    
    def __init__(self, record_id, first_name, last_name, middle_name=None, home_phone=None,cell_phone=None, 
        work_phone=None, street_address=None, po_box=None, city=None, country=None, employer_name=None, employer_phone=None, 
        employer_street_address=None, employer_po_box=None, employer_city=None, employer_country=None ):
        self.record_id = record_id
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.home_phone = home_phone
        self.cell_phone = cell_phone
        self.work_phone = work_phone
        self.street_address = street_address
        self.po_box = po_box
        self.city = city
        self.country = country
        self.employer_name= employer_name
        self.employer_phone= employer_phone
        self.employer_street_address=  employer_street_address
        self.employer_po_box = employer_po_box
        self.employer_city = employer_city
        self.employer_country = employer_country


class Users(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.String(255), primary_key=True)
    role= db.Column(db.String(255))
    username = db.Column(db.String(80), unique=True)
    first_name= db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email= db.Column(db.String(255), unique= True)
    password = db.Column(db.String(255), unique=True)
    date_joined = db.Column(db.DateTime)

    def __init__(self, user_id,role, username,first_name,last_name,email, password, date_joined):
        self.user_id = user_id
        self.role = role
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(password,method='pbkdf2:sha256')
        self.date_joined = date_joined

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.user_id)  # python 2 support
        except NameError:
            return str(self.user_id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)



