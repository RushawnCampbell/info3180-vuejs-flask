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