import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from lask_login import LoginManager

login_manager = LoginManager()

app= Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
basedir= os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABATE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')#DB location
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db =SQLAlchemy(app)
Migrate(app,db)

login_manager.init_app(app)
login_manager.login_view = 'login'
