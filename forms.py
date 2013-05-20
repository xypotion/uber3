from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField, validators, ValidationError

class ContactForm(Form):
  name = TextField("Name", [validators.Required("Name required")])
  email = TextField("Email", [validators.Required("Email required"), validators.Email("Email must be valid")])
  subject = TextField("Subject", [validators.Required("Subject required")])
  message = TextAreaField("Message", [validators.Required("Message required")])
  submit = SubmitField("Send")