from application import app
from flask import render_template, request

@app.route("/user/new/")
def tasks_form():
    return render_template("user/new.html")

@app.route("/user/", methods=["POST"])
def user_create():
    U  = User(request.form.get("name"))
    N  = User(request.form.get("nick"))
   
    return "Toimi!"
