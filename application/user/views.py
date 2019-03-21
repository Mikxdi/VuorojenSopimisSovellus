from application import app
from flask import render_template, request

@app.route("/user/new/")
def tasks_form():
    return render_template("user/new.html")

@app.route("/user/", methods=["POST"])
def tasks_create():
    print(request.form.get("name"))
  
    return "Toimi!"
