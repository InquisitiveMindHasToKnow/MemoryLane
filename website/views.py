from flask import Blueprint, render_template


# All routes / pages users can navigate to
views = Blueprint('views', __name__)

# this function runs whenever we go to home page
@views.route('/')
def home():
    return render_template("home.html")