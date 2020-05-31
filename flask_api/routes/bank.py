from flask import Blueprint, jsonify, request
from flask_api.extensions import db
from flask_api.models import Users, Banks
from flask_jwt_extended import jwt_required, get_jwt_identity


bank_routes = Blueprint('bank_routes', __name__)


@bank_routes.route('/bank/add', methods=["POST"])
@jwt_required
def add_bank():

    account_number = request.json.get('bank_no', None)

    bank_name = request.json.get('bank_name', None)

    email = get_jwt_identity()
    
    # for debugging
    # email = request.json.get('email', None)
    print(email)

    user = Users.query.filter_by(email=email).first()

    # If user doesn't exist
    if user is None:
        print("User doesn't exist'")
        return jsonify({"msg": "User doesn't exist"}), 400

    potential_bank = (Banks.query.filter_by(account_number=account_number)
                      .first())

    # If bank account is currently in use
    if potential_bank is not None:
        print("Bank in use")
        return jsonify({"msg": "Bank in use"}), 409

    # if user does not have a bank account, add to Banks table
    if user.banks is None:
        bank = Banks(account_number=account_number,
                     bank_name=bank_name,
                     email=email)

        db.session.add(bank)
        db.session.commit()

        return jsonify({"msg": ""}), 201

    # if the user already has a bank account, send back error
    else:
        print('User already has a bank')
        return jsonify({"msg": "User already has a bank"}), 409


@bank_routes.route('/bank', methods=["GET"])
@jwt_required
def get_banks():

    email = get_jwt_identity()

    user = Users.query.filter_by(email=email).first()

    if user is None:
        print('User doesnt exist')
        return jsonify({"msg": "User doesn't exit"}), 400

    user_bank = user.banks
    print(user_bank)
    if user.banks:
        bank_number = user_bank.account_number
        print('Bank act num: ' + str(bank_number))

        bank_name = user_bank.bank_name
        print('Bank name: ' + str(bank_name))

        return jsonify({"banks": [{"bank_name": bank_name,
                                   "bank_no": bank_number}]}), 200

    else:
        print('User doesnt have a bank yet')
        return jsonify({"msg": "User doesn't have a bank yet"}), 204


@bank_routes.route('/bank/deposit', methods=["POST"])
@jwt_required
def deposit():

    print(request)
    bank_no = request.json.get('bank_no', None)
    amount = request.json.get('amount', None)
    email = get_jwt_identity()

    user = Users.query.filter_by(email=email).first()

    if user is None:
        print("User doesn't exist")
        return jsonify({"msg": "User doesn't exit"}), 400

    user_bank = user.banks
    print(user_bank)

    if bank_no != user_bank.account_number:
        print('That bank account is not on file')
        return jsonify({"msg": "Bank account not on file"}), 400

    else:
        if user.account_balance - amount >= 0:
            user.account_balance -= amount
            db.session.commit()
            print(user.account_balance)
            return jsonify({"msg": "Withdrawal successful"}), 200

        else:
            return jsonify({"msg": "Can't withdraw more than your\
                                    account balance"}), 406


@bank_routes.route('/bank/withdraw', methods=["POST"])
@jwt_required
def withdraw():

    bank_no = request.json.get('bank_no', None)
    amount = request.json.get('amount', None)
    email = get_jwt_identity()

    user = Users.query.filter_by(email=email).first()

    if user is None:
        return jsonify({"msg": "User doesn't exit"}), 400

    user_bank = user.banks

    if bank_no != user_bank.account_number:
        print(user_bank.account_number)
        print(bank_no)
        return jsonify({"msg": "Bank account not on file"}), 400

    else:
        user.account_balance += amount
        db.session.commit()
        print(user.account_balance)
        return jsonify({"msg": "Deposit Successful"}), 200
