from flask import Blueprint,render_template,url_for,redirect
from datetime import datetime
from flask_login import current_user , login_required

showauth = Blueprint("showauths",__name__)
@showauth.route("/show_auth/<token>/")
@login_required
def showauths(token):
    if current_user.is_authenticated:
        from app import Auths,db,Apps
        get_email = Apps.query.filter_by(token=token).first()
        if current_user.email == get_email.email:
            auths_list = Auths.query.filter_by(token=token).all()
            current_app = Apps.query.filter_by(token=token).first()
            return render_template("show_auth.html",app_name=current_app.name,logged=True,username=current_user.username,authlist=auths_list)
        else:
            return redirect(url_for("dash.dash"),405)
    return redirect(url_for("login.login"))