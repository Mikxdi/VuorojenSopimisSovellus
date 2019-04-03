
from application.suggestion.models import Suggestion
from application import app
from flask import render_template, request, url_for, redirect
from application import db
from application.suggestion.forms import SuggestionForm

@app.route("/suggestion/new/")
def suggestion_form():
    return render_template("suggestion/new.html", form=SuggestionForm())

@app.route("/suggestion/", methods=["POST"])
def suggestion_create():
    form = SuggestionForm(request.form)
    if not form.validate():
        return render_template("suggestion/new.html", form=form)
    n = Suggestion(form.name.data, form.when.data)

    db.session().add(n)
    db.session().commit()
    return redirect(url_for("index"))

