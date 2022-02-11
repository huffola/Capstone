#dungeons_and_devs/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

#######################################################
#################DATABASE SETUP########################
#######################################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')#sets connection to DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#create DATABASE object
db = SQLAlchemy(app)
Migrate(app,db)#connects application to the database



#######################################################
#######################################################
#######################################################



#######################################################
###############LOGIN CONFIGURATIONS####################
#######################################################

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'



#######################################################
#######################################################
#######################################################


#grabbing blueprint from core/views.py & registering it
from dungeons_and_devs.core.views import core
#grabbing blueprint from .py & registering it
from dungeons_and_devs.users.views import users
#grabbing blueprint from error_pages/handlers.py & registering it
from dungeons_and_devs.error_pages.handlers import error_pages
#grabbing blueprint from posts/views.py & registering it
from dungeons_and_devs.posts.views import characters

#BLUEPRINTS
app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
app.register_blueprint(characters)
