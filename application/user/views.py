from application import app
from flask import render_template, request

@app.route("/user/new/")
def user_form():
    return render_template("user/new.html")

@app.route("/user/", methods=["POST"])
def user_create():
    n = User(request.form.get("name"))
    nn = User(request.form.get("nick"))

    db.session().add(n)
    db.session().add(nn)
    db.session().commit()
 
    return "Käyttäjä lisätty"
