from flask import Blueprint,render_template,url_for
from flask_login import current_user
homepage = Blueprint("home",__name__)
@homepage.route("/")
@homepage.route("/home")
def home():
    if current_user.is_authenticated:
        return render_template("homepage.html",logged=True,username=current_user.username)
    return render_template("homepage.html")