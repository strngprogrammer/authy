
from flask import Blueprint,render_template,url_for,request,flash,redirect
from models.Models import Register
from werkzeug.security import generate_password_hash
signuppage = Blueprint("signup",__name__)
@signuppage.route("/signup",methods=["GET","POST"])
@signuppage.route("/register",methods=["GET","POST"])
def signup():
    
    form = Register()
    if form.validate_on_submit():
        from app import User , db
        email = User.query.filter_by(email=form.email.data).first()
        username = User.query.filter_by(username=form.username.data).first()
        if not username and not email:
            hashed_password = generate_password_hash(form.password.data,method='sha256')
            new_user = User(name=form.name.data,email=form.email.data,username=form.username.data,password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("login.login"))
        if email:
            flash("email already exist","error")
        if username:
            flash("username already exist","error")
        return render_template("signuppage.html",field=form)
    return render_template("signuppage.html",field=form)