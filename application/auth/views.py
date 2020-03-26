from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app,db
from application.auth.models import User
from application.auth.forms import LoginForm
from application.auth.forms import RegisterForm
@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))   

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/register")
def register_form():
    return render_template("auth/registerform.html", form = RegisterForm())

@app.route("/auth/register", methods=["POST"])
def auth_register():
    form = RegisterForm(request.form)

    r = User(form.username.data, form.password.data)

    db.session().add(r)

    db.session().commit()
    
    return redirect(url_for("auth_login"))