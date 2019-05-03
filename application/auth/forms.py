from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus", [validators.Length(min=4, max=20, message='Merkkien määrän tulee olla väliltä 4-20')])
    password = PasswordField("Salasana", [validators.Length(min=4, max=20, message='Merkkien määrän tulee olla väliltä 4-20')])
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=4, max=20, message='Merkkien määrän tulee olla väliltä 4-20')])
    username = StringField("Käyttäjätunnus", [validators.Length(min=4, max=20, message='Merkkien määrän tulee olla väliltä 4-20')])
    password = PasswordField("Salasana", [validators.Length(min=4, max=20, message='Merkkien määrän tulee olla väliltä 4-20')])

    class Meta:
        csrf = False
