"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request, url_for
from CheckAddress import app

from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
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

    submit = SubmitField('Submit')

"""
    "Routes
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
    oAddress = AddressForm()

    if request.method == "POST":
        return redirect(url_for('home'))
    
    return render_template(
        'address.html',
        title = 'Address',
        year = datetime.now().year,
        fAddress = oAddress
    )


