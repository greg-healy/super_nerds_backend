from flask import Blueprint, jsonify, request
from flask_api.models import Users, Transactions, UsersTransactions
from flask_api.extensions import db
from datetime import datetime

requests = Blueprint('requests', __name__)


@requests.route('/send', methods=['POST'])
def send():
    # For testing purposes, user will be the email in the request:
    user = request.json.get('requestor', None)

    # user = get_jwt_identity()

    recipient = request.json.get('email', None)
    amount = request.json.get('amount', None)
    
    user = Users.query.filter_by(email=user).first()
    recipient = Users.query.filter_by(email=recipient).first()
    
    if user is None:
        print('User doesnt exist')
        return jsonify({"msg": "User doesn't exit"}), 400
    
    if recipient is None:
        print('Recipient doesnt exist')
        return jsonify({"msg": "User doesn't exit"}), 400
    
    # Subtract the money from the user's account_balance
    print("User's starting balance " + str(user.account_balance))
    print("Recipient's starting balance " + str(user.account_balance))

    user.account_balance -= amount
    recipient.account_balance += amount

    db.session.commit()
    
    print("User's balance after sending " + str(user.account_balance))
    print("Recipient's balance after sending " + str(recipient.account_balance))

    # Add the money to the recipient's account_balance

    # TODO: Add a transaction to the transactions table

    today = datetime.now()
    print("Today's date:", today)

    transaction = Transactions(transaction_date=today,
                               amount_transfered=amount)
    
    db.session.add(transaction)
    db.session.commit()

    senders_transaction = UsersTransactions(email=user.email,
                                             transaction_id=transaction.transaction_id,
                                             sender=True)   
    
    recipient_transaction = UsersTransactions(email=recipient.email,
                                               transaction_id=transaction.transaction_id,
                                               sender=False)

    db.session.add(senders_transaction)
    db.session.add(recipient_transaction)
    db.session.commit()                   
    
    return jsonify({"msg": "Success"}), 200


@requests.route('/request/all', methods=['GET'])
def request_all():

    # # email = get_jwt_identity()
    # email = request.json.get('email', None)
    
    # user = Users.query.filter_by(email=email).first()

    # if user is None:
    #     return jsonify({"msg": "User doesn't exit"}), 400

    # email = user.email
    # first_name = user.first_name
    # last_name = user.last_name
    
    # # requests table
    # amount 

    # # requests table
    # req_id

    # # User reqs table
    # requestor
        
    return("Request All is working")



@requests.route('/request/new', methods=['POST'])
def request_new():

    return("Request New is working")

