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



 
@views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        # Handle profile picture upload
        picture = request.files['profile_picture']

        if picture:
            # Define where to save the uploaded picture in the profile_pictures folder
            picture_filename = secure_filename(picture.filename)
            picture_save = os.path.join('website/static/profile_pictures', picture_filename)

            # Save/update the current user's profile picture in the database
            current_user.profile_picture = picture_filename
            db.session.commit()

            # Save the uploaded picture to the specified location
            picture.save(picture_save)

            # Flash message
            flash('Profile picture successfully updated!', category='success')
            return redirect(url_for('views.profile'))

    return render_template("profile.html", user=current_user)