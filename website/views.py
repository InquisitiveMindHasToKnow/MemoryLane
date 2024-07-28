from flask import Blueprint, render_template
from flask_login import login_required, current_user



# All routes / pages users can navigate to
views = Blueprint('views', __name__)

# this function runs whenever we go to home page
@views.route('/')
@login_required # can't get to home page unless logged in
def home():
    return render_template("home.html", user=current_user)