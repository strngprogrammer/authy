from flask import Blueprint, redirect,render_template,url_for,request,flash
from models.Models import LoginField
from werkzeug.security import check_password_hash
from flask_login import login_user
loginpage = Blueprint("login",__name__)
@loginpage.route("/login",methods=["GET","POST"])
@loginpage.route("/signin",methods=["GET","POST"])
def login():
    form = LoginField()
    if form.validate_on_submit():
        from app import User
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password,form.password.data):
                login_user(user,remember=form.checkbox.data)
                return redirect(url_for("home.home"))
        flash("user or password is incorrect!!")
        return render_template("loginpage.html",field=form)
    return render_template("loginpage.html",field=form)