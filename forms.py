# forms.py
"""Forms for our pet app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField,IntegerField
from wtforms.validators import InputRequired, Optional

class AddPetForm(FlaskForm):
    """Form for adding pet."""

    name = StringField("Pet Name",validators=[InputRequired()])
    species=StringField("species",validators=[InputRequired()])
    photo_url=StringField("Picture url",validators=[Optional()])
    ages=IntegerField("Pet age",validators=[Optional()])
    notes=StringField("Pet notes",validators=[Optional()])
    available=BooleanField("available for adoption",validators=[InputRequired()])



