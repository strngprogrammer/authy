from flask import Blueprint,render_template,url_for,redirect
from datetime import datetime
from flask_login import current_user , login_required
from models.Models import NewApp
from secrets import token_hex
newapppage = Blueprint("newapp",__name__)
@newapppage.route("/newapp",methods=["GET","POST"])
@login_required
def newapp():
    form = NewApp()
    if current_user.is_authenticated:
        from app import Apps,db
        if form.validate_on_submit():
            now = datetime.today().strftime('%Y-%m-%d')
            new_app = Apps(name=form.name.data,password=form.password.data,date=now,auths=0,email=current_user.email,token=str(token_hex(8)*2))
            db.session.add(new_app)
            db.session.commit()
            return redirect(url_for("dash.dash"))
        return render_template("newapp.html",logged=True,username=current_user.username,form=form)
    return redirect(url_for("login.login"))