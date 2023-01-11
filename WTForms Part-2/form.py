from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField
import email_validator
from wtforms import validators, ValidationError


class ContactForm(FlaskForm):
    name = TextField('Enter Your Name',[validators.required('Please enter your name!')])
    gender = RadioField('Gender',choices=[('M','male'),("F",'female'),('O','other')])
    address = TextAreaField('Address')
    email = TextAreaField('Email',[validators.required('Please enter your E-Mail Address'),
                                    validators.Email('Please enter a valid E-Mail Address')])

    age = IntegerField('Age')
    language = SelectField('Languages Known',choices=[('cpp','C++'),('py','Python'),('java','Java')])

    submit = SubmitField('Submit')
