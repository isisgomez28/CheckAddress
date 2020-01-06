"""
Routes and views for the flask application.
"""

import os
from datetime import datetime
from flask import render_template, request, url_for, redirect
from flask_uploads import UploadSet

from CheckAddress import app

from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField
from wtforms import StringField, TextField, SubmitField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from werkzeug.utils import secure_filename
from wtforms.validators import DataRequired, Length

"""
    Forms
"""
class AddressForm(FlaskForm):
    """Address form."""
    street1 = StringField('Street1', [
        DataRequired(),
        Length(min = 4, message=('Your street name is to short'))])
    street2 = StringField('Street2')
    apartment = StringField('Apartment', [
        DataRequired(),
        Length(min = 2, message=('Your apartment name is to short'))])
    state = StringField('State', [
        DataRequired()])
    sector = StringField('Sector', [
        DataRequired()])
    notes = StringField('Notes')

    frontDoor = FileField('Front Door', validators=[
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])

    recaptcha = RecaptchaField()

    submit = SubmitField('Submit')

"""
    Routes
"""
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/address', methods=('GET', 'POST'))
def address():
    oAddress = AddressForm(csrf_enabled=False)

    if oAddress.validate_on_submit():
        f = oAddress.frontDoor.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(
            app.instance_path, 'photos', filename
        ))
        return redirect(url_for('home'))
    
    return render_template(
        'address.html',
        title = 'Address',
        year = datetime.now().year,
        form = oAddress
    )


