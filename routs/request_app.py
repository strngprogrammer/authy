from flask import Blueprint,render_template,url_for,redirect
from datetime import datetime
from flask_login import current_user , login_required

requestapp = Blueprint("request_app",__name__)
@requestapp.route("/request_app/<token>/")
@login_required
def request_app(token):
    if current_user.is_authenticated:
        from app import Auths,db,Apps
        get_email = Apps.query.filter_by(token=token).first()
        if current_user.email == get_email.email:
            current_app = Apps.query.filter_by(token=token).first()
            return render_template("request_app.html",current_app=current_app, logged=True,username=current_user.username)
        else:
            return redirect(url_for("dash.dash"),405)
    return redirect(url_for("login.login"))