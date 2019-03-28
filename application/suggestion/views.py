
from application.suggestion.models import Suggestion
from application import app
from flask import render_template, request

@app.route("/suggestion/new/")
def suggestion_form():
    return render_template("suggestion/new.html")

@app.route("/suggestion/", methods=["POST"])
def suggestion_create():
    n = Suggestion(request.form.get("name"))
    w = Suggestion(request.form.get("when"))

    db.session().add(n, w)
    db.session().commit()
  
    return "hello world!"

