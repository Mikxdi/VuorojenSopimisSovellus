from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators
  
class LocationForm(FlaskForm):
    name = StringField("Nimi", [validators.input_required(message="Anna paikan nimi"), validators.length(min=4, max=30, message='Merkkien määrä on oltava välillä 4-30')])
    price = IntegerField("Hinta euroina", [validators.number_range(min=10, max=1000, message='Hinnan on oltava väliltä 10-1000 euroa')])
  
    class Meta:
        csrf = False
