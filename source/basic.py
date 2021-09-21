from flask import Flask, render_template, session , redirect, url_for
from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField, DateTimeField, TextField, TextAreaField, SelectField
from wtforms.validators import DataRequired


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class RegisterForm(FlaskForm):
    email = StringField("Email:", validators=[DataRequired()])
    username = StringField("Username:", validators=[DataRequired()])
    password = StringField("Password:", validators=[DataRequired()])
    password_confirm = StringField("Retype Password:", validators=[DataRequired()])
    phone_num = StringField("Phone Number(optional):")
    gender =RadioField('Select your desired gender:', choices=[('gender_male', 'Male'), ('gender_fem','Female'), ('gender_oth','Other')])
    submit = SubmitField('SUBMIT')



@app.route('/')
def index():
    return render_template('home.html')

@app.route('/profile')
def profile():
    bag = ['Judge','Zone','Truth','Explorer','Evader','Valkryie','Felon','Rive']
    return render_template('profile.html',bag=bag)

@app.route('/my_bag')
def my_bag():
    return render_template('my_bag.html')

@app.route('/friends')
def friends():
    return render_template('friends.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    form = RegisterForm
    if form.validate_on_submit():
        session['email'] = form.email.data
        session['username'] = form.username.data
        session['password'] = form.password.data
        session['password_confirm'] = form.password_confirm.data
        session['phone_num'] = form.phone_num.data
        session['gender'] = form.gender.data

        return redirect(url_for('index'))
    return render_template('signup.html', form=form)

@app.route('/disc_finder')
def disc_finder():
    return render_template('disc_finder.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
