from flask import Blueprint, render_template, request


# User auth blueprint 
auth = Blueprint('auth', __name__)

@auth.route('sign-up', methods=['GET', 'POST']) #method allows us to decide what kind of request we can accept in the route.
def sign_up():
    data = request.form
    return render_template('sign_up.html')  

@auth.route('login', methods=['GET', 'POST'])
def login():
    data = request.form
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p>Testing Logout page</p>"

