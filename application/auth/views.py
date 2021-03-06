from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
  
from application import app
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import RegisterForm
from application import db

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                                error = "Väärä käyttäjätunnus tai salasana")


    login_user(user)
    return redirect(url_for("index")) 

@app.route("/auth/register", methods=["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/registerform.html", form=RegisterForm())

    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("auth/registerform.html", form=form)

    u = User(form.name.data, form.username.data, form.password.data, 'user')



    db.session().add(u)
    db.session().commit()

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form=form,
                error="Käyttäjänimi tai salasana väärin")

    print("Käyttäjä " + user.name + " tunnistettiin")
    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))   
