from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError


#Building VARS for Login FlaskForm
class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(),Email()])
    password = PasswordField('Password', validators = [DataRequired())
    submit = SubmitField('Login')

#Building VARS for Registration FlaskForm
class RegistrationForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(),Email()])
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired(),EqualTo('pass_confirm',message='Passwords must match.')])
    pass_confirm = PasswordField('Username', validators = [DataRequired()])
    submit = SubmitField('Register')

    #checks to see if email is already in use
    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('email is already in use.')

    #checks to see if username is already in use
    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('username is already in use.')
