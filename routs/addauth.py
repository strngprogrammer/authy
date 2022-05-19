
from flask import Blueprint,render_template,url_for,redirect
from datetime import datetime
from flask_login import current_user , login_required
from models.Models import NewAuth
from secrets import token_hex
import time,threading

from routs.newapp import newapp

def calc(days,sep,Auths,Apps,db):
    day = int(days)

    while day != 0 :
        time.sleep(24*3600)
        old = Auths.query.filter_by(uniqevalue=sep).first()
        old.days-=1
        day-=1
        db.session.commit()
    auth1 = Auths.query.filter_by(uniqevalue=sep).first()
    last_auth = Apps.query.filter_by(token=auth1.token).all()
    last_auth[-1].auths -= 1
    db.session.delete(auth1)
    db.session.commit()



addauth = Blueprint("addat",__name__)
@addauth.route("/addauth/<token>/",methods=["GET","POST"])
@login_required
def addat(token):
    form = NewAuth()
    if current_user.is_authenticated:
        from app import Auths,db,Apps
        if form.validate_on_submit():
            get_email = Apps.query.filter_by(token=token).first()
            print(get_email)
            if current_user.email == get_email.email:
                new_app = Auths(name=form.name.data,email=current_user.email,token=token,auth=form.auth.data,days=int(form.days.data),uniqevalue=str(token_hex(8)*2))
                db.session.add(new_app)
                last_auth = Apps.query.filter_by(token=token).all()
                last_auth[-1].auths += 1
                db.session.commit()
                t = threading.Thread(target=calc,args=(new_app.days,new_app.uniqevalue,Auths,Apps,db), daemon=True)
                t.start()
                return redirect(url_for("dash.dash"))
            else:
                return redirect(url_for("dash.dash"),405)
        current_app = Apps.query.filter_by(token=token).first()
        return render_template("addauth.html",app_name=current_app.name,logged=True,username=current_user.username,form=form)
    return redirect(url_for("login.login"))