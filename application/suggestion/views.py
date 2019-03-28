

from application import app
from flask import render_template, request

@app.route("/suggestion/new/")
def tasks_form():
    return render_template("suggestion/new.html")

@app.route("/suggestion/", methods=["POST"])
def tasks_create():
    print(request.form.get("name"))
    print(request.form.get("when"))

  
    return "hello world!"

