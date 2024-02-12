#store all standard routes where users can only go to...
from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os
from . import db
#view blueprint
#defining name of blueprint
views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template('home.html', user=current_user)  #rendering the home.html page from templates folder

 
@views.route('/profile')
@login_required
def profile():
    if request.method == 'POST':
        #Handle profile picture
        picture = request.files['profile_picture']
        
        if picture:
            #defines where to save the uploaded picture and in the profile_pictures folder
            picture_filename = secure_filename(picture.filename)
            picture_save = (os.path.join('website/static/profile_pictures', picture_filename))
            
            #And finally save/update the current user's profile picture in the database
            current_user.profile_picture = picture_filename
            db.session.commit()
            
            #A flash
            flash('Profile picture successfully Updated!!', category='success')
            return redirect(url_for('views.profile'))

    
    return render_template("profile.html", user=current_user)


@views.route('/upload_picture', methods=['POST'])
@login_required
def upload_picture():
    # This route is used by the form in the profile template to handle file uploads
    # It redirects back to the profile route after handling the upload
    return redirect(url_for('views.profile'))