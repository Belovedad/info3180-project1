from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object(__name__)
# Config Values

app.config['UPLOAD_FOLDER'] = "./app/static/uploads"
app.config['SECRET_KEY'] = "random"
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://pro1:pro1@localhost/pro1"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bhelaruohnruww:b156672b02fac7d95779fd2ce642174fce05c44779183f52379bf947a85af1a2@ec2-23-23-195-205.compute-1.amazonaws.com:5432/dapv42qhjrsc6i'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

db = SQLAlchemy(app)

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session

from app import views