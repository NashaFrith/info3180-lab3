from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired

class MyForm(FlaskForm):
    name = StringField('Name',validators=[InputRequired()])
    email = StringField('Email',validators=[InputRequired()])
    subject = StringField('Subject',validators=[InputRequired()])
    message = TextAreaField('Message',validators=[InputRequired()])