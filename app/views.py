"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template, request, jsonify, send_file
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
from app.models import Users
from app.forms import LoginForm
import os


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


@app.route('/api/register', methods=['POST'])
def register():
    return ''

@app.route('/api/auth/login', methods=['POST'])
def login():
    def login():
        loginform = LoginForm()
        if request.method == "POST":
            if  loginform.validate_on_submit():
                username = loginform.username.data
                password = loginform.password.data
                user = Users.query.filter_by(username=username).first()
                if user is not None and check_password_hash(user.password, password):
                    login_user(user)
                    #flash('You are now logged in.', 'success')
                    return jsonify({
                            "message": "Login Successful",
                            "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNjE4MDI5MjE4LCJleHAiOjE2MTgwMjkyMTh9.PiLE3syBXnEYfKqTiSmEPz1HN0D7jkAI9BjmrfjyGAI"
                        }),200
                else:
                    return jsonify({
                            "message": "Login failed, check your information and try again.",
                        }),401
                   
        return ''

@app.route('/api/auth/logout', methods=['POST'])
@login_required
def logout():
    if current_user.is_authenticated:
        logout_user()
        return jsonify({
            "message": "Log out successful"
        }),200

@app.route('/api/cars', methods=['GET', 'POST'])
@login_required
def cars():
    if current_user.is_authenticated:
        return ''

@app.route('/api/cars/{car_id}', methods=['GET'])
@login_required
def singlecar(car_id):
    if current_user.is_authenticated:
        return ''

@app.route('/api/cars/{car_id}/favourite', methods=['POST'])
@login_required
def favourite(car_id):
    if current_user.is_authenticated:
        return ''

@app.route('/api/search', methods=['GET'])
@login_required
def singlecar():
    if current_user.is_authenticated:
        return ''

@app.route('/api/users/{user_id}', methods=['GET'])
@login_required
def singlecar(user_id):
    if current_user.is_authenticated:
        return ''

@app.route('/api/users/{user_id}/favourites', methods=['GET'])
@login_required
def singlecar(user_id):
    if current_user.is_authenticated:
        return ''

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)

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