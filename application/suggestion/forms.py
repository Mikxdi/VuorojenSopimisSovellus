from flask_wtf import FlaskForm
from wtforms import StringField, validators
  
class SuggestionForm(FlaskForm):
    name = StringField("Nimi", [validators.input_required(message="Anna vuoron nimi")])
    when = StringField("Milloin", [validators.input_required(message="Anna aika")])
  
    class Meta:
        csrf = False
