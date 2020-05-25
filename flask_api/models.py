# Create models (database tables) in this file
from .extensions import db


class Users(db.Model):
    email = db.Column(db.String(128), primary_key=True)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    password = db.Column(db.String(32))
    account_balance = db.Column(db.Float)

    # One to One Relationship
    banks = db.relationship('Banks', backref='users', uselist=False)


class Banks(db.Model):
    account_number = db.Column(db.Integer, primary_key=True,
                               autoincrement=False)
    bank_name = db.Column(db.String(32))
    email = db.Column(db.String(128), db.ForeignKey('users.email'))


class Transactions(db.Model):
    transaction_id = db.Column(db.Integer, primary_key=True)
    transaction_date = db.Column(db.DateTime)
    transaction_desc = db.Column(db.String(255))
    amount_transfered = db.Column(db.Float)

# mapping table for Many-Many Relationship

db.Table('Users_Transactions',
         db.Column('user_id', db.Integer, db.ForeignKey('users.email')),
         db.Column('transaction_id', db.Integer, db.ForeignKey('transactions.transaction_id')),
         db.Column('sender', db.Boolean))

class Requests(db.Model):
    req_id = db.Column(db.Integer, primary_key=True)
    amount_req = db.Column(db.Float)
    req_status = db.Column(db.Boolean)

db.Table('Users_Reqs',
         db.Column('user_id', db.Integer, db.ForeignKey('users.email')),
         db.Column('req_id', db.Integer, db.ForeignKey('requests.req_id')),
         db.Column('requestor', db.Boolean))
