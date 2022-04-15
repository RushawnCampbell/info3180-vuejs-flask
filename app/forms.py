from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email, InputRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class UploadForm(FlaskForm):
    fileField = FileField('image upload',validators=[FileRequired(),FileAllowed(['jpg', 'png', 'jpeg'], 'Illegal file detected. You must enter an image')])

class ContactForm(FlaskForm):
    name = StringField("Please enter your fullname", validators=[DataRequired()])
    email = EmailField("Please enter your e-mail address", validators=[DataRequired(), Email()])
    subject = StringField("Please enter the subject for your message", validators=[DataRequired()])
    message = TextAreaField("Please enter the message you would like to send", validators=[DataRequired()], render_kw={"rows": "3"})


       