
from flask import Blueprint,render_template,url_for,redirect,request


requestraw = Blueprint("request_raw",__name__)
@requestraw.route("/request_raw/")
def request_raw():
    from app import Auths
    try:
        token = request.headers["token"]
        name = request.headers["name"]
        auths = Auths.query.filter_by(token=token).all()
        allthis = ""
        for au in auths:
            allthis += (au.auth + "\n")
        return allthis
    except:
        return "missing info"