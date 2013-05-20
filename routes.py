import os
from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.secret_key = 'ancestral recall'

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db = SQLAlchemy(app)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form = ContactForm()

	if request.method == "POST":
		if form.validate() == False:
		  flash('All fields are required.')
		  return render_template('contact.html', form=form)
		else:
		  return 'Form posted.'

	elif request.method == "GET":
		return render_template('contact.html', form=form)

if __name__ == '__main__':
  app.run(debug=True)