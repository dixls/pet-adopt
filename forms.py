from tokenize import String
from unicodedata import name
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, BooleanField, URLField
from wtforms.validators import InputRequired, Optional


class AddPetForm(FlaskForm):
    """Form for adding a new pet"""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField(
        "Species", choices=[("dog", "Dog"), ("cat", "Cat"), ("porcupine", "Porcupine")]
    )
    photo_url = URLField("Photo URL")
    age = IntegerField("Age")
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField()
