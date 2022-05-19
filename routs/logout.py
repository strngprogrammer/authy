from flask import Blueprint, redirect,render_template,url_for,request,flash
from flask_login import logout_user , login_required
logoutpage = Blueprint("logout",__name__)
@logoutpage.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login.login"))