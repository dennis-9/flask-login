#store all standard routes where users can only go to...
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user



#auth blueprint
#defining name of blueprint
auth = Blueprint('auth', __name__)

#all routes will be here login, logout and signup
@auth.route('/login', methods=['GET','POST'])  #user goes to /login and sends a get or post request
def login():  #this function is called when the user accesses this route
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        #checking if fields are empty or valid
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in Successfully!', category= "success")
                login_user(user, remember=True)  #remember me feature, maybe when the user clears his browser FLASK is gonna remember, that this user has already logged in
                return redirect(url_for('views.home'))
            else:
                flash("Invalid Password", category="error")
        else:
            flash('Email does not exist!', category= "error")
            
    return render_template("login.html", user=current_user)  #render the login page from templates/login.html

@auth.route("/logout")
@login_required   #decorator that checks if user is logged in before allowing them to view the page
def logout():     #function called when user navigates to /logout
    logout_user()  #logs out the user
    flash('You have been logged out successfully!', category='info')
    return redirect(url_for('auth.login'))  #redirects user back to login page

@auth.route("/sign-up", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Check form validation
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')

        elif not email or len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')

        elif not first_name or len(first_name) < 2:
            flash('First Name must be greater than 1 character.', category='error')

        elif not password1 or password1 != password2 or len(password1) < 7:
            flash('Invalid password. It should have at least 7 characters.', category='error')

        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Hurray!! Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)#renders the sign up page from templates/signup.html
