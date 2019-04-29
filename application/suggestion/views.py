
from application.suggestion.models import Suggestion, Vote
from application import app, login_required
from flask import render_template, request, url_for, redirect
from application import db
from application.suggestion.forms import SuggestionForm
from flask_login import current_user
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
@login_required(role = "ANY")
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
@login_required(role = "ANY")
def suggestion_list():
    return render_template("suggestion/list.html", form = SuggestionForm(), sugg = Suggestion.query.all())

@app.route("/suggestion/remove/<suggId>", methods=["POST"])
@login_required(role = "ANY")
def suggestion_remove(suggId):
    for votes in Vote.query.filter_by(suggestion_id = suggId):
        votes.query.delete()
    Suggestion.query.filter_by(id=suggId).delete()
    db.session().commit()
    return redirect(url_for("suggestion_list"))

@app.route("/suggestion/edit/<suggId>", methods = ["POST", "GET"])
@login_required(role = "ANY")
def suggestion_edit(suggId):
    suggUpdate = Suggestion.query.get(suggId)

    form = SuggestionForm(request.form)
    form.name.data = suggUpdate.name
    form.when.data = suggUpdate.when
    form.location.data = suggUpdate.location

    if request.method == "GET":
        return render_template("suggestion/edit.html" , form = form, suggestion = suggUpdate)

    if not form.validate():
        return render_template("suggestion/edit.html", form=form)
    
    form = SuggestionForm(request.form)
    suggUpdate.name = form.name.data
    suggUpdate.when = form.when.data
    suggUpdate.location = form.location.data

    db.session().commit()
    return redirect(url_for("suggestion_list"))

@app.route("/suggestion/vote/<suggId>", methods = ["POST"])
@login_required(role = "ANY")
def suggestion_vote(suggId):
    voted = Vote.query.filter(Vote.suggestion_id == suggId).filter(Vote.account_id == current_user.id).all()
    if voted:
        return redirect(url_for("suggestion_list"))
    
    nVote = Vote(suggId, current_user.id)
    db.session().add(nVote)
    db.session().commit()

    votes = Vote.query.filter(Vote.suggestion_id == suggId).count()
    if votes >= 10:
        suggTrue = Suggestion.query.get(suggId)
        suggTrue.success = True
        db.session().commit()
    return redirect(url_for("suggestion_list"))
