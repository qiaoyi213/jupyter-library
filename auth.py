from flask import Blueprint, render_template, request

auth_flask_login = Blueprint('auth_flask_login', __name__, template_folder="templates")

@auth_flask_login.route('/login', method=["GET", "POST"])
def login():
    if request.method == "POST" and "email" in request.form:
        email = request.form['email']
        userObj = User()
        user = userObj.
        if user and flask_bcrypt
        
