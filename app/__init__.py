from flask import Flask
from flask_mail import Mail
app = Flask(__name__)
app.config['SECRET_KEY'] = 'lul69'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525' # (or try 2525)
app.config['MAIL_USERNAME'] = '29393c420efea0'
app.config['MAIL_PASSWORD'] = 'aba314d0937626'
mail = Mail(app)
from app import views