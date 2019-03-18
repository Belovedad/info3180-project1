"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os,datetime
from sqlalchemy import exc
from app import app,db
from flask import render_template, request, redirect, url_for, flash,jsonify, make_response
from .forms import AddForm
from flask_mail import Message
from werkzeug.utils import secure_filename
from .models import UserProfile
from flask_sqlalchemy import SQLAlchemy



###
# Routing for your application.
###


@app.route('/profile', methods=["GET","POST"])
def profile():
    """Render add profiile page"""
    form = AddForm()

    if request.method == 'POST':
        filefolder = app.config['UPLOAD_FOLDER']
        if form.validate_on_submit():
            fname = request.form["fname"]
            lname = request.form["lname"]
            gender = request.form["gender"]
            email = request.form["email"]
            location = request.form["location"]
            biography = request.form["biography"]
            
            file = request.files['fileupload']
            filename = secure_filename(file.filename)
            file.save(os.path.join(filefolder, filename))
            created_on = datetime.date.today()
            user = UserProfile(fname, lname, gender, email, location, biography, filename, created_on)
            db.session.add(user)
            db.session.commit()
            
            
            flash('Profile added successfully')
            return redirect(url_for('profiles'))
    
    return render_template('newprof.html', form=form)

@app.route("/profiles")
def profiles():
    users = UserProfile.query.all()
    profiles = []
    for user in users:
        profiles.append({"pp": user.pp, "fname":user.fname, "lname": user.lname, "gender": user.gender, "location":user.location, "id":user.id})
    
    return render_template("profilel.html", profiles = profiles)
    
@app.route('/profile/<userid>')

def getprof(userid):
    user = UserProfile.query.filter_by(id=userid).first()
    
    if user is None:
        return redirect(url_for('home'))
        
    
    return render_template("singprof.html", user=user)

def format_date_joined(date):
    return date.strftime("%B,%Y")


@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
