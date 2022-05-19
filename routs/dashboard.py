from flask import Blueprint,render_template,url_for,redirect
from flask_login import current_user , login_required
dashboard = Blueprint("dash",__name__)
@dashboard.route("/dashboard")
@login_required
def dash():
    if current_user.is_authenticated:
        from app import Apps
        apps = Apps.query.filter_by(email=current_user.email).all()
        return render_template("dashboard.html",logged=True,username=current_user.username,apps=apps)
    return redirect(url_for("login.login"))