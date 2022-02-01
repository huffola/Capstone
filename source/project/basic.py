from flask import Flask, render_template, flash, session , redirect, url_for, abort
from flask import request
from flask_login import login_user, login_required, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField, DateTimeField, TextField, TextAreaField, SelectField
from wtforms.validators import DataRequired
import os
from flask_sqlalchemy import SQLAlchemy
#from source import app, db
#from source.models import User
#from source.forms import LoginForm, RegistrationForm


basedir= os.path.abspath(os.path.dirname(__file__))#setting path for DB
app = Flask(__name__)








#///////////////////////////////////////////////////////////////
#COMMENTED OUT BECAUSE THIS IS ALREADY IN FORMS.PY
#class RegisterForm(FlaskForm):
#    email = StringField("Email:", validators=[DataRequired()])
#    username = StringField("Username:", validators=[DataRequired()])
#    password = StringField("Password:", validators=[DataRequired()])
#    password_confirm = StringField("Retype Password:", validators=[DataRequired()])
#    phone_num = StringField("Phone Number(optional):")
#    gender =RadioField('Select your desired gender:', choices=[('gender_male', 'Male'), ('gender_fem','Female'), ('gender_oth','Other')])
#    submit = SubmitField('SUBMIT')

#HOME PG///////////////////////////////////////////////////////////////
@app.route('/')
def index():
    return render_template('home.html')

#PROFILE PG///////////////////////////////////////////////////////////////
@app.route('/profile')
def profile():
    bag = ['Judge','Zone','Truth','Explorer','Evader','Valkryie','Felon','Rive']
    return render_template('profile.html',bag=bag)

#COLLECTIONS PG///////////////////////////////////////////////////////////////
@app.route('/collections')
def collections():
    return render_template('collections.html')

#GAME RULES PG///////////////////////////////////////////////////////////////
@app.route('/game_rules')
def game_rules():
    return render_template('game_rules.html')

#GAME RULES PG///////////////////////////////////////////////////////////////
@app.route('/sourcebooks')
def sourcebooks():
    return render_template('sourcebooks.html')

#REGISTER PG (referencing the registerform class)///////////////////////////////////////////////////////////////
@app.route('/signup', methods=['GET','POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():

        session['email'] = form.email.data
        session['username'] = form.username.data
        session['password'] = form.password.data
        session['password_confirm'] = form.password_confirm.data
        session['phone_num'] = form.phone_num.data
        session['gender'] = form.gender.data
        flash('Thanks for registering!')


        return redirect(url_for('profile'))
    return render_template('signup.html', form=form)

#ERROR handler PG///////////////////////////////////////////////////////////////
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
