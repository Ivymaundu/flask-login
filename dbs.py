from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import sessionmaker
from flask_login import UserMixin,LoginManager

app = Flask(__name__)
app.secret_key="secretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:12345@localhost:5432/myduka_class"


db = SQLAlchemy(app)
# login_manager for instanting the flask_login extention

login_manager=LoginManager()
login_manager.init_app(app)

class User(UserMixin,db.Model):
    __tablename__="user"
    id=db.Column(db.Integer,primary_key=True,nullable=False)
    name=db.Column(db.String(100))
    email=db.Column(db.String(100),unique=True)
    password=db.Column(db.String(100))



@login_manager.user_loader
def load_user(users_id):
    cont = User.query.get(int(users_id))
    return cont 



