from flask import Blueprint


# User auth blueprint 
auth = Blueprint('auth', __name__)

@auth.route('sign-up')
def sign_up():
    return "<p> Testing sign up page</p>"

@auth.route('login')
def login():
    return "<p>Testing Login page</p>"

@auth.route('/logout')
def logout():
    return "<p>Testing Logout page</p>"

