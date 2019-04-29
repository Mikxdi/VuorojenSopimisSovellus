from application.location.models import Location
from application import app, login_required
from flask import render_template, request, url_for, redirect
from application import db
from application.location.forms import LocationForm
from application.suggestion.models import Suggestion
from application.suggestion.models import Vote

@app.route("/location/new/")
def location_form():
    return render_template("location/new.html", form=LocationForm())

@app.route("/location/", methods=["POST"])
@login_required(role = "ANY")
def location_create():
    form = LocationForm(request.form)

    n = Location(form.name.data, form.price.data)

    db.session().add(n)
    db.session().commit()
    return redirect(url_for("location_list"))

@app.route("/location/", methods=["GET"])
@login_required(role = "ANY")
def location_list():
    return render_template("location/list.html", form = LocationForm(), loc = Location.query.all())

@app.route("/location/remove/<locId>", methods=["POST"])
@login_required(role = "ANY")
def location_remove(locId):
    for suggestions in Suggestion.query.filter_by(location_id = locId):
        for votes in Vote.query.filter_by(suggestion_id = suggestions.id):
            votes.query.delete()
        suggestions.query.delete()
    Location.query.filter_by(id=locId).delete()
    db.session().commit()
    return redirect(url_for("location_list"))


@app.route("/location/edit/<locId>", methods=["POST", "GET"])
@login_required(role="ANY")
def location_edit(locId):
    locUpdate = Location.query.get(locId)

    form = LocationForm(request.form)
    form.name.data = locUpdate.name
    form.price.data = locUpdate.price

    if request.method == "GET":
        return render_template("location/edit.html" , form = form, location = locUpdate)

    if not form.validate():
        return render_template("location/edit.html", form=form)
    
    form = LocationForm(request.form)
    locUpdate.name = form.name.data
    locUpdate.price = form.price.data

    db.session().commit()
    return redirect(url_for("location_list"))