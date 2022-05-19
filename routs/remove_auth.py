from flask import Blueprint, redirect,render_template,url_for,request,flash
from flask_login import current_user , login_required
removeauth = Blueprint("remove_auth",__name__)
@removeauth.route("/remove_auth/<token>/<auth>/")
@login_required
def remove_auth(token,auth):
    from app import db,Apps,Auths
    get_email = Auths.query.filter_by(token=token).first()
    if current_user.email == get_email.email:
        auth1 = Auths.query.filter_by(uniqevalue=auth).first()
        last_auth = Apps.query.filter_by(token=token).all()
        last_auth[-1].auths -= 1
        db.session.delete(auth1)
        db.session.commit()
        return redirect(f"/show_auth/{token}/")
    else:
        return redirect(url_for("dash.dash"),405)