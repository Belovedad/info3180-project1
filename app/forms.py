from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired,FileAllowed

class AddForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()])
    gender = SelectField('Gender',choices = [('Male', 'Male'), ('Female', 'Female')])
    email = StringField('E-mail', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    biography = TextAreaField('Biography', validators=[DataRequired()]) 
    fileupload=FileField('image',validators=[FileRequired(),FileAllowed(['jpg', 'png',])])
    