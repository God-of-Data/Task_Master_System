
from flask import Blueprint, render_template

from user.user import User

user = Blueprint("user", __name__)



@user.route("/user/signin/")
def show_sign_in_page():

    return render_template("signin.html")


@user.route("/user/signup/")
def show_sign_up_page():

    return render_template("signup.html")


@user.route("/user/signin_action/", methods = ["POST"])
def sign_in():

    existing_user = User()

    return existing_user.sign_in()


@user.route("/user/signup_action/", methods = ["POST"])
def sign_up():

    new_user = User()

    return new_user.sign_up()


@user.route("/user/signout_action/")
def sign_out():

    connected_user = User()

    return connected_user.sign_out()
