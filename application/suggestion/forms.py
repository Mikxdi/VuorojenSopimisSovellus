from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.fields.html5 import DateField
  
class SuggestionForm(FlaskForm):
    name = StringField("Nimi", [validators.input_required(message="Anna vuoron nimi")])
    when = DateField("Milloin", format='%yyyy-%mm-%dd')
  
    class Meta:
        csrf = False
