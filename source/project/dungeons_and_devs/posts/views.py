#posts/views.py
#creating updating and deleting character views
from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import current_user,login_required
from dungeons_and_devs import db
from dungeons_and_devs.models import Character
from dungeons_and_devs.posts.forms import CreateCharacterForm

characters = Blueprint('characters',__name__)
######################CRUDCRUDCRUDCRUDCRUD######################################
###CREATING A CHARACTER VIEW
@characters.route('/create',methods=['GET','POST'])
@login_required
def create_character():
    form = CreateCharacterForm()

    if form.validate_on_submit():

        character = Character(name=form.name.data,
                              level=form.level.data,
                              class_=form.class_.data,
                              saves=form.saves.data,
                              race=form.race.data,
                              gender=form.gender.data,
                              age=form.age.data,
                              weight=form.weight.data,
                              hair=form.hair.data,
                              eyes=form.eyes.data,
                              notes=form.notes.data,
                              user_id=current_user.id)
        db.session.add(character)
        db.session.commit()
        flash('Character Created')
        return redirect(url_for('core.index'))

    return render_template('create_character.html',form=form)

###VIEWING A CHARACTER
@characters.route('/<int:character_id>')
def character(character_id):
    character = Character.query.get_or_404(character_id)
    return render_template('character.html',name=character.name,
                                           level=character.level,
                                           class_=character.class_,
                                           saves=character.saves,
                                           race=character.race,
                                           gender=character.gender,
                                           age=character.age,
                                           weight=character.weight,
                                           hair=character.hair,
                                           eyes=character.eyes,
                                           notes=character.notes)

###UPDATING A CHARACTER
@characters.route('/<int:character_id>/update',methods=['GET','POST'])
@login_required
def update(character_id):
    character = Character.query.get_or_404(character_id)

    if character.owner != current_user:
        abort(403)

    form = CreateCharacterForm()
    if form.validate_on_submit():

        character.name=form.name.data
        character.level=form.level.data
        character.class_=form.class_.data
        character.saves=form.saves.data
        character.race=form.race.data
        character.gender=form.gender.data
        character.age=form.age.data
        character.weight=form.weight.data
        character.hair=form.hair.data
        character.eyes=form.eyes.data
        character.notes=form.notes.data

        db.session.commit()
        flash('Character Updated')
        return redirect(url_for('characters.character', character_id=character.id))

    elif request.method == 'GET':
        form.name.data = character.name
        form.level.data = character.level
        form.class_.data = character.class_
        form.saves.data = character.saves
        form.race.data = character.race
        form.gender.data = character.gender
        form.age.data = character.age
        form.weight.data = character.weight
        form.hair.data = character.hair
        form.eyes.data = character.eyes
        form.notes.data = character.notes



    return render_template('create_character.html',form=form)


###DELETING A CHARACTER
@characters.route('/<int:character_id>/delete',methods=['GET','POST'])
@login_required
def delete_charcter(character):
    character = Character.query.get_or_404(character_id)

    if character.owner != current_user:
        abort(403)

    db.session.delete(character)
    db.session.commit()
    flash('Character Successfully Deleted')
    return redirect(url_for('core.index'))
