from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object(__name__)
# Config Values

app.config['UPLOAD_FOLDER'] = "./app/static/uploads"
app.config['SECRET_KEY'] = "random"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://pro1:pro1@localhost/pro1"
#app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://zleemoztxzukqn:aa2a37bbc783f15ce145e52e75b6ca4ad371b6ff4011bc00ad6873939b708797@ec2-75-101-133-29.compute-1.amazonaws.com:5432/d9lrtd31pctolg'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session

from app import views