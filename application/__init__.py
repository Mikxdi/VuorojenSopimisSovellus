from flask import Flask
app = Flask(__name__)

from application import views

from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///suggestion.db"

app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application import views


from application.user import models
from application.user import views


db.create_all()
