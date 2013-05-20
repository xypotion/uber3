from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)

    def __init__(self, username, email):
        self.username = username

    def __repr__(self):
        return '<User %r>' % self.username