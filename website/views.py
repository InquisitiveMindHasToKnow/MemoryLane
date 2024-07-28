from flask import Blueprint


# All routes / pages users can navigate to
views = Blueprint('views', __name__)

# this function runs whenever we go to home page
@views.route('/')
def home():
    return "<h1> Testing Homepage route </>"