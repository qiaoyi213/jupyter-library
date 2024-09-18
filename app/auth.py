from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import LoginManager

from app import db
from app.models.user import User

# Create Blueprint
auth_blueprint = Blueprint("auth_blueprint", __name__, template_folder="templates")

# Initialize Login Manager
login_manager = LoginManager()
# login_manager.login_view = "auth.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth_blueprint.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user:
            flash("user already exists")
            return redirect(url_for("auth_blueprint.register"))
        new_user = User(username=username)
        new_user.set_password(password)
        print(new_user.password_hash)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please Login")
        print("SUCCESS")
        return redirect(url_for("auth_blueprint.login"))

    return render_template("auth/register.html")


@auth_blueprint.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()

        if not user:
            flash("user do not exists")
            return redirect(url_for("auth_blueprint.login"))

        if user.check_password(password) == False:
            flash("password wrong")
            return redirect(url_for("auth_blueprint.login"))

        # check user information
        flash("Login Successful")
        return redirect(url_for("auth_blueprint.dashboard"))

    return render_template("auth/login.html")


@auth_blueprint.route("/dashboard")
def dashboard():
    return render_template("auth/dashboard.html")
