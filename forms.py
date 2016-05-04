from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators, ValidationError
 
class ContactForm(Form):
  name = TextField("Name", [validators.Required("Please enter your name.")])
  email = TextField("Email", [validators.Required("Please enter your email address"), validators.Email()])
  bookname = TextField("Book Name", [validators.Required("Please enter the associated book name.")])
  message = TextAreaField("Message", [validators.Required("Please enter your comment/review.")])
  submit = SubmitField("Send")