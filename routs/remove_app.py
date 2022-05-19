from flask import Blueprint, redirect,render_template,url_for,request,flash
from flask_login import current_user , login_required
removeapp = Blueprint("remove_app",__name__)
@removeapp.route("/remove_app/<token>/")
@login_required
def remove_app(token):
    from app import db,Apps,Auths
    get_email = Apps.query.filter_by(token=token).first()
    if current_user.email == get_email.email:
        this_app = Apps.query.filter_by(token=token).first()
        all_auths = Auths.query.filter_by(token=token).all()
        for auth in all_auths:
            db.session.delete(auth)
        db.session.delete(this_app)
        db.session.commit()
        return redirect(url_for("dash.dash"))
    else:
        return redirect(url_for("dash.dash"),405)