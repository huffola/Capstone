from source import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


#load users allows flask loging to load the current user and grab their # ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



###THIS FILE CREATES VIEWS/TABLES for the * DATABASE *

class User(db.Model,UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)#this ensures primary keys are used in this TABLES
    email = db.Column(db.String(64),unique = True, index = True)
    username = db.Column(db.String(64),unique = True, index = True)
    password_hash = db.Column(db.String(128))

    #creating instance of this object
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    #checking if the user credentials are correct
    def check_password(self, ppassword):
        return check_password_hash(self.password_hash,password)
