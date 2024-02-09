#store all standard routes where users can only go to...
from flask import Blueprint, render_template
from flask_login import login_required, current_user

#view blueprint
#defining name of blueprint
views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template('home.html', user=current_user)  #rendering the home.html page from templates folder

 
