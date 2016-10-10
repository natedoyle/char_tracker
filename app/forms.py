from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class DND5e(Form):
    name = StringField('Character Name', validators=[DataRequired()])
    strength = StringField('Str', validators=[DataRequired()])
    dexterity = StringField('Dex', validators=[DataRequired()])
    constitution = StringField('Con', validators=[DataRequired()])
    intelligence = StringField('Int', validators=[DataRequired()])
    wisdom = StringField('Wis', validators=[DataRequired()])
    charisma = StringField('Cha', validators=[DataRequired()])
    # turn to dropdown and give add option for multi-class
    char_class = StringField('Class(es)', validators=[DataRequired()])
    levels = StringField('Level(s)', validators=[DataRequired()])
    hps = StringField('HPs', validators=[DataRequired()])
    armor_class = StringField('AC', validators=[DataRequired()])

class ThirteenthAge(DND5e):
    one_unique_thing = StringField('One Unique Thing', validators=[DataRequired()])