#users/views.py
from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user,current_user,logout_user,login_required
from dungeons_and_devs import db#THIS is in __init__ sql alchemy object
from dungeons_and_devs.models import User,Character #,Compendium
from dungeons_and_devs.users.forms import RegistrationForm,LoginForm,UpdateUserForm
from dungeons_and_devs.users.picture_handler import add_profile_pic

users = Blueprint('users',__name__)

#VIEWS WE WANT TO see
#register
@users.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    #creates a valid user object
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Successfully Registered')
        return redirect(url_for('users.login'))
    return render_template('register.html',form=form)


#login
@users.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    #validates user
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Login Success')
            #if user is trying to access a user specific pg without being logged in
            next = request.args.get('next')
            if next == None or not next[0]=='/':
                next = url_for('core.index')
            return redirect(next)
        return render_template('login.html',form=form)
    return render_template('login.html',form=form)


#logout
@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("core.index"))


#account (update userform)
@users.route("/account",methods=['GET','POST'])
@login_required
def account():
    form = UpdateUserForm()

    if form.validate_on_submit():
        print(form)
        if form.picture.data:
            username = current_user.username
            pic = add_profile_pic(form.picture.data,username)
            current_user.profile_image = pic

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('User Account Updated')
        return redirect(url_for('users.account'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    profile_image = url_for('static', filename='profile_pics/' + current_user.profile_image)
    return render_template('account.html', profile_image=profile_image, form=form)

#users character(s)####3THIS PORTION WILL DIFFER FROM B-POSTS
@users.route("/<username>")
def user_characters(username):
    page = request.args.get('page', 1, type=int) #each pg refers to 1 character(this allows users to cycle through each character individually)

    user = User.query.filter_by(username=username).first_or_404()

    characters = Character.query.filter_by(owner=user).order_by(Character.name.asc()).paginate(page=page, per_page=5)#lists characters in ascneding order by name

    return render_template('user_characters.html', characters=characters, user=user)



#entire compendium view!!! (BIG ONE)
