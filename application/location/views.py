from application.location.models import Location
from application import app
from flask import render_template, request, url_for, redirect
from application import db
from application.location.forms import LocationForm
from flask_login import login_required
from application.suggestion.models import Suggestion

@app.route("/location/new/")
def location_form():
    return render_template("location/new.html", form=LocationForm())

@app.route("/location/", methods=["POST"])
@login_required
def location_create():
    form = LocationForm(request.form)

    n = Location(form.name.data, form.price.data)

    db.session().add(n)
    db.session().commit()
    return redirect(url_for("location_list"))

@app.route("/location/", methods=["GET"])
@login_required
def location_list():
    return render_template("location/list.html", form = LocationForm(), loc = Location.query.all())

@app.route("/location/remove/<locId>", methods=["POST"])
@login_required
def location_remove(locId):
    for suggestions in Suggestion.query.filter_by(location_id = locId):
        suggestions.query.delete()
    Location.query.filter_by(id=locId).delete()
    db.session().commit()
    return redirect(url_for("location_list"))