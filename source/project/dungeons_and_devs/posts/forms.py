#posts/formy.py
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,IntegerField
from wtforms.validators import DataRequired

class CreateCharacterForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired()])
    level = IntegerField('Level')
    class_ = StringField('Class')
    saves = IntegerField('Saves')
    race = StringField('Race',validators=[DataRequired()])
    gender = StringField('Gender')
    age = IntegerField('Age')
    weight = IntegerField('Weight')
    hair = StringField('Hair Color')
    eyes = StringField('Eye Color')
    notes = StringField('Character Notes')

    submit = SubmitField("Create")
