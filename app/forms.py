from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField, EmailField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, InputRequired


class SigninForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    fullname = StringField("Fullname", validators=[DataRequired()])
    email = EmailField("Email Address", validators=[DataRequired(), Email()])

class QuickSearchForm(FlaskForm):
    quicksearch = StringField('quicksearch', validators=[InputRequired()])

class AddSkiptrace(FlaskForm):
    first_name= StringField('First Name')
    middle_name = StringField('Middle Name')
    last_name= StringField('Last Name')
    nib = StringField('N.I.B#')
    dob= StringField('D.O.B')
    gender= StringField('Gender')
    marital_status= StringField('Marital Status')
    home_phone= StringField('Home Phone')
    cell_phone = StringField('Cell Phone')
    work_phone = StringField('Work Phone')
    street_address= StringField('street Address')
    po_box = StringField('P.O Box')
    city= StringField('City')
    country= StringField('Country')
    emp_first_name= StringField('First Name')
    emp_middle_name = StringField('Middle Name')
    emp_last_name= StringField('Last Name')
    emp_phone= StringField('Phone')
    emp_street_address= StringField('street Address')
    emp_po_box = StringField('P.O Box')
    emp_city= StringField('City')
    kin_first_name= StringField('First Name')
    kin_middle_name = StringField('Middle Name')
    kin_last_name= StringField('Last Name')
    kin_street_address= StringField('street Address')
    kin_po_box = StringField('P.O Box')
    kin_city= StringField('City')
    kin_country= StringField('Country')
    kin_emp_first_name= StringField('First Name')
    kin_emp_middle_name = StringField('Middle Name')
    kin_emp_last_name= StringField('Last Name')
    kin_emp_phone= StringField('Phone')
    kin_emp_street_address= StringField('street Address')
    kin_emp_po_box = StringField('P.O Box')
    kin_emp_city= StringField('City')
    kin_emp_country= StringField('Country')


class ModSkiptrace(FlaskForm):
    first_name= StringField('First Name')
    middle_name = StringField('Middle Name')
    last_name= StringField('Last Name')
    nib = StringField('N.I.B#')
    dob= StringField('D.O.B')
    gender= StringField('Gender')
    marital_status= StringField('Marital Status')
    home_phone= StringField('Home Phone')
    cell_phone = StringField('Cell Phone')
    work_phone = StringField('Work Phone')
    street_address= StringField('street Address')
    po_box = StringField('P.O Box')
    city= StringField('City')
    country= StringField('Country')
    emp_first_name= StringField('First Name')
    emp_middle_name = StringField('Middle Name')
    emp_last_name= StringField('Last Name')
    emp_phone= StringField('Phone')
    emp_street_address= StringField('street Address')
    emp_po_box = StringField('P.O Box')
    emp_city= StringField('City')
    kin_first_name= StringField('First Name')
    kin_middle_name = StringField('Middle Name')
    kin_last_name= StringField('Last Name')
    kin_street_address= StringField('street Address')
    kin_po_box = StringField('P.O Box')
    kin_city= StringField('City')
    kin_country= StringField('Country')
    kin_emp_first_name= StringField('First Name')
    kin_emp_middle_name = StringField('Middle Name')
    kin_emp_last_name= StringField('Last Name')
    kin_emp_phone= StringField('Phone')
    kin_emp_street_address= StringField('street Address')
    kin_emp_po_box = StringField('P.O Box')
    kin_emp_city= StringField('City')
    kin_emp_country= StringField('Country')


class ModUser(FlaskForm):
    first_name= StringField('First Name')
    last_name= StringField('Last Name')
    role= SelectField(label='Role', choices=[('Skiptracer', 'Skiptracer'), ('Admin', 'Admin')])
    username = StringField('Last Name')
    email = EmailField("Email Address", validators=[DataRequired(), Email()])


"""class CarForm(FlaskForm):
    make = StringField('Make', validators=[InputRequired()])
    model = StringField('Model', validators=[InputRequired()])
    colour = StringField("Colour", validators=[DataRequired()])
    year = StringField("Year", validators=[DataRequired()])
    price = StringField("Price", validators=[DataRequired()])
    car_type = SelectField(label='Car Type', choices = [('Hatchback','hatchback'),('Sedan','sedan'), ('SUV','suv'), ('MUV','muv'), ('Coupe','coupe'), ('Convertible','convertible'), ('Pickup Truck','pickuptruck') ])
    transmission = SelectField(label='Transmission', choices=[('Automatic', 'automatic'), ('Manual', 'manual')])
    description = TextAreaField("Description", validators=[DataRequired()], render_kw={"rows": "3"})
    photo = FileField('image upload',validators=[FileRequired(),FileAllowed(['jpg', 'png', 'jpeg'], 'Illegal file detected. You must enter an image')])

"""