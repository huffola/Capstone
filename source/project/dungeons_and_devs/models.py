#models.py
from dungeons_and_devs import db,login_manager
from werkzeug import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader#allows for user authentication in templates(html pages)
def load_user(user_id):
    return User.query.get(user_id)


#setting up classes_tables

class User(db.Model,UserMixin):#establishing TABLE DESIGN


    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    profile_image = db.Column(db.String(64),nullable=False,default='default_profile.png')
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))

    characters = db.relationship('Character',backref='owner',lazy=True)#specifies that an Owner of a Character is a User Model/Table

    #enables the creation of a user instance
    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"Username: {self.username}"




class Character(db.Model):#establishing TABLE DESIGN

    users = db.relationship(User)

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)#CONNECTS CHARACTER TO USER!!!!!!!
    ###THINK ABOUT fields for CHARACTER TIMESTAMP (16:30) in Models Setup video
    #Name, race, gender, level, class, abilities, attacks,
    # feats, skills, equipment, age, weight, hair, eyes, player, saves, attributes, notes
    name = db.Column(db.String(64),index=True,nullable=False)
    race = db.Column(db.String(64),index=True,nullable=False)
    gender = db.Column(db.String(25),index=True)
    level = db.Column(db.Integer,index=True)
    class_ = db.Column(db.String(25),index=True)
    age = db.Column(db.Integer,index=True)
    weight = db.Column(db.Integer,index=True)
    hair = db.Column(db.String(25),index=True)
    eyes = db.Column(db.String(25),index=True)
    saves = db.Column(db.Integer,index=True)
    notes = db.Column(db.String(255),index=True)

    #character_image = db.Column(db.String(64),nullable=False,default='default_profile.png')


    #init method to make an instance of a characters
    def __init__(self,name,race,gender,level,class_,age,weight,hair,eyes,saves,notes,user_id):
        self.name = name
        self.race = race
        self.gender = gender
        self.level = level
        self.class_ = class_
        self.age = age
        self.weight = weight
        self.hair = hair
        self.eyes = eyes
        self.saves = saves
        self.notes = notes
        self.user_id = user_id

    def __repr__(self):
        return f"Character ID: {self.id}"


#need to load parsed data here!!!!
#class Compendium(db.Model):#establishing TABLE DESIGN
#    pass
