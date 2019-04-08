from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField 
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class RegisterForm(FlaskForm):
    name = StringField("Nimi")
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana")

    class Meta:
        csrf = False
