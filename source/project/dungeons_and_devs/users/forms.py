#form based imports
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed
#user based imports
from flask_login import current_user
from dungeons_and_devs.models import User

#####LOGIN FORM######
class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Log In')

#####Registration FORM######
class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),EqualTo('pass_confirm',message='Passwords must match.')])
    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register')

    #check to see if email is already in use
    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')
    #check to see if username is already in use
    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')

#####Update user FORM######
class UpdateUserForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    #below ensures that only jpgs and pngs may be added
    picture = FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Apply Changes')

    #check to see if email is already in use
    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')
    #check to see if username is already in use
    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')
