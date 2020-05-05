# Create models (database tables) in this file
from .extensions import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    email = db.Column(db.String(128))
    password = db.Column(db.String(32))


class Banks(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
