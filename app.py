from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,UserMixin
app = Flask(__name__)
app.config["SECRET_KEY"] = "u6qyetr896etr6tywrev34"
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'


db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login.login"
class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(120),unique=True,nullable=False)
    username = db.Column(db.String(32),unique=True,nullable=False)
    password = db.Column(db.String(250),unique=False,nullable=False)

    def __repr__(self) -> str:
        return super().__repr__()

class Apps(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(120),nullable=False)
    password = db.Column(db.String(250),unique=False,nullable=False)
    date = db.Column(db.String(250),unique=False,nullable=False)
    auths = db.Column(db.Integer)
    token = db.Column(db.String(250),unique=True,nullable=False)

class Auths(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(120),nullable=False)
    token = db.Column(db.String(250),unique=False,nullable=False)
    auth = db.Column(db.String(250),unique=False,nullable=False)
    days = db.Column(db.Integer,primary_key=False)
    uniqevalue = db.Column(db.String(250),unique=True,nullable=False)
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
from routs.home import homepage
from routs.login import loginpage
from routs.signup import signuppage
from routs.logout import logoutpage
from routs.dashboard import dashboard
from routs.newapp import newapppage
from routs.addauth import addauth
from routs.showauths import showauth
from routs.remove_app import removeapp
from routs.remove_auth import removeauth
from routs.request_app import requestapp
from routs.request_raw import requestraw


app.register_blueprint(homepage)
app.register_blueprint(loginpage)
app.register_blueprint(signuppage)
app.register_blueprint(logoutpage)
app.register_blueprint(dashboard)
app.register_blueprint(newapppage)
app.register_blueprint(addauth)
app.register_blueprint(showauth)
app.register_blueprint(removeapp)
app.register_blueprint(removeauth)
app.register_blueprint(requestapp)
app.register_blueprint(requestraw)

if __name__=="__main__":
    app.run(debug=True)