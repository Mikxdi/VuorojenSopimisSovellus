from application.location.models import Location
from application import app
from flask import render_template, request, url_for, redirect
from application import db
from application.location.forms import LocationForm
from flask_login import login_required

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
    return redirect(url_for("index"))