from flask import Blueprint, jsonify, request
from flask_api.models import Users, Transactions, UsersTransactions
from datetime import datetime

transactions = Blueprint('transactions', __name__)

@transactions.route('/activity', methods=['GET'])
def activity():
    user_logged_in = request.json.get('email', None)    

    user = Users.query.filter_by(email=user_logged_in).first()

    if user is None:
         return jsonify({"msg": "User doesn't exit"}), 400

    user_transactions = UsersTransactions.query.filter_by(email=user.email).all()

    transaction_list = []

    for i in user_transactions:
        transactions = Transactions.query.filter_by(transaction_id=i.transaction_id).all()

        for j in transactions:
            other_user_rows = UsersTransactions.query.filter(UsersTransactions.transaction_id==j.transaction_id).filter(UsersTransactions.email!=i.email).all()

            for x in other_user_rows:
                other_user = Users.query.filter_by(email=x.email).first()
                date = str(j.transaction_date.month) + "/" + str(j.transaction_date.day) + "/" + str(j.transaction_date.year)

                list_item = {"email": x.email, 
                            "first_name": other_user.first_name,
                            "last_name": other_user.last_name,
                            "sender": x.sender,
                            "amount": j.amount_transfered,
                            "date": date}

                #print(list_item)
                transaction_list.append(list_item)              
                

    return jsonify(transaction_list), 200