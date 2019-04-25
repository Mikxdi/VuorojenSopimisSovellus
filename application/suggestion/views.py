
from application.suggestion.models import Suggestion
from application import app
from flask import render_template, request, url_for, redirect
from application import db
from application.suggestion.forms import SuggestionForm
from flask_login import login_required
from application.location.models import Location
 
@app.route("/suggestion/new/")
def suggestion_form():
    form = SuggestionForm()
    locations = []
    for location in Location.query.all():
        label = location.name 
        locations.append((location.id, label))
    form.location.choices = locations
    return render_template("suggestion/new.html", form=form)

@app.route("/suggestion/", methods=["POST"])
@login_required
def suggestion_create():
    form = SuggestionForm(request.form)
    locations = []
    for location in Location.query.all():
        label = location.name
        locations.append((location.id, label))
    form.location.choices = locations
    if not form.validate():
        return render_template("suggestion/new.html", form=form)

    
    n = Suggestion(form.name.data, form.when.data, form.location.data, False)

    db.session().add(n)
    db.session().commit()
    return redirect(url_for("suggestion_list"))

@app.route("/suggestion/", methods=["GET"])
@login_required
def suggestion_list():
    return render_template("suggestion/list.html", form = SuggestionForm(), sugg = Suggestion.query.all())