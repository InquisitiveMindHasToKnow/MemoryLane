from flask import Blueprint, render_template


# User auth blueprint 
auth = Blueprint('auth', __name__)

@auth.route('sign-up')
def sign_up():
    return render_template('sign_up.html')
@auth.route('login')
def login():
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p>Testing Logout page</p>"

