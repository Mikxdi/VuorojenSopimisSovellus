from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators
  
class LocationForm(FlaskForm):
    name = StringField("Nimi", [validators.input_required(message="Anna vuoron nimi")])
    price = IntegerField("Hinta")
  
    class Meta:
        csrf = False
