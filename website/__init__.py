from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()

#creating a variable for the db
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    #encrypt the cookies insertion data
    app.config['SECRET_KEY'] = 'my_secret_key'
    # So my sqlite database is stored here
    app. config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    #initialize the database by giving it a flask app
    
    db.init_app(app)

    
    #registering the blueprints here
    #telling flask that we have some blueprints that contain differnt views
    from .views import views
    from .auth import auth
    
    #register them
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User
    
    with app.app_context():
        db.create_all()
        
    #where do we need to go  when someone logs in or signs up? 
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    #this is telling  flask how to get the current user or how to load a  user
    @login_manager.user_loader
    def load_user(user_id):
        #returns a user object if the id matches one in the database
        return User.query.get(int(user_id))
    

    return app

#use a path module, check if db exists....if does not it will create one
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')