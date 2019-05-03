from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, validators
from wtforms.fields.html5 import DateField
  
class SuggestionForm(FlaskForm):
    name = StringField("Nimi", [validators.input_required(message='Anna vuoron nimi'), validators.Length(min=4, max=30, message='Merkkien määrän tulee olla väliltä 4-30')])
    when = DateField("Milloin", [validators.data_required(message='Anna päivämäärä')])
    location = SelectField("Missä", coerce=int)
  
    class Meta:
        csrf = False
