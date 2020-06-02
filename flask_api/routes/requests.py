from flask import Blueprint, jsonify, request
from flask_api.models import (Users, Transactions, UsersTransactions,
                              Requests, UsersReqs)
from flask_api.extensions import db
from datetime import datetime
from flask_jwt_extended import jwt_required, get_jwt_identity

requests = Blueprint('requests', __name__)


def send_money(user_logged_in, recipient, amount):
    user = Users.query.filter_by(email=user_logged_in).first()
    recipient = Users.query.filter_by(email=recipient).first()

    if user is None:
        print('User doesnt exist')
        return jsonify({"msg": "User doesn't exit"}), 400

    if recipient is None:
        print('Recipient doesnt exist')
        return jsonify({"msg": "User doesn't exit"}), 400

    # Subtract the money from the user's account_balance
    print("User's starting balance " + str(user.account_balance))
    print("Recipient's starting balance " + str(recipient.account_balance))

    user.account_balance -= amount
    recipient.account_balance += amount

    db.session.commit()

    # Add the money to the recipient's account_balance

    today = datetime.now()
    print("Today's date:", today)

    transaction = Transactions(transaction_date=today,
                               amount_transfered=amount)

    db.session.add(transaction)
    db.session.commit()

    senders_transaction = UsersTransactions(
                              email=user.email,
                              transaction_id=transaction.transaction_id,
                              sender=True)

    recipient_transaction = UsersTransactions(
                                email=recipient.email,
                                transaction_id=transaction.transaction_id,
                                sender=False)

    db.session.add(senders_transaction)
    db.session.add(recipient_transaction)
    db.session.commit()


@requests.route('/send', methods=['POST', 'GET'])
@jwt_required
def send():
    # For testing purposes, user will be the email in the request:
    user = get_jwt_identity()

    # user = get_jwt_identity()

    recipient = request.json.get('email', None)
    amount = request.json.get('amount', None)

    send_money(user, recipient, amount)

    return jsonify({"msg": "Success"}), 200


@requests.route('/request/all', methods=['GET'])
@jwt_required
def request_all():

    # email = get_jwt_identity()
    user_logged_in = get_jwt_identity()
    user = Users.query.filter_by(email=user_logged_in).first()
    print(user_logged_in)

    if user is None:
        return jsonify({"msg": "User doesn't exit"}), 400

    # all user requests linked to the logged in user
    user_is_requestor_reqs = (UsersReqs.query.
                              filter(UsersReqs.email == user_logged_in).
                              filter(UsersReqs.requestor == True).all())

    user_is_requestee_reqs = (UsersReqs.query.
                              filter(UsersReqs.email == user_logged_in).
                              filter(UsersReqs.requestor == False).all())

    sent_requests = []
    recv_requests = []

    # all requests
    for i in user_is_requestor_reqs:
        requests = Requests.query.filter_by(req_id=i.req_id).all()

        for j in requests:
            other_user_rows = (UsersReqs.query.
                               filter(UsersReqs.req_id == j.req_id).
                               filter(UsersReqs.email != i.email).all())

            for x in other_user_rows:
                other_user = Users.query.filter_by(email=x.email).first()

                list_item = {"email": x.email,
                             "first_name": other_user.first_name,
                             "last_name": other_user.last_name,
                             "amount": j.amount_req,
                             "req_id": j.req_id,
                             "requestor": True}

                sent_requests.append(list_item)

    for i in user_is_requestee_reqs:
        requests = Requests.query.filter_by(req_id=i.req_id).all()

        for j in requests:
            other_user_rows = (UsersReqs.query.
                               filter(UsersReqs.req_id == j.req_id).
                               filter(UsersReqs.email != i.email).all())

            for x in other_user_rows:
                other_user = Users.query.filter_by(email=x.email).first()

                list_item = {"email": x.email,
                             "first_name": other_user.first_name,
                             "last_name": other_user.last_name,
                             "amount": j.amount_req,
                             "req_id": j.req_id,
                             "requestor": True}

                recv_requests.append(list_item)

    all_requests = {"sent_requests": sent_requests,
                    "recv_requests": recv_requests}

    print(all_requests)

    return jsonify(all_requests), 200


@requests.route('/request/new', methods=['POST'])
@jwt_required
def request_new():

    # Using until we add JWT
    user_logged_in = get_jwt_identity()
    print(user_logged_in)

    requestee = request.json.get('email', None)
    print(requestee)

    amount = request.json.get('amount', None)
    print(amount)

    # Do we need this?
    is_requestor = request.json.get('is_requestor', None)
    print(is_requestor)

    # Add the request

    users_request = Requests(amount_req=amount, req_status=True)
    db.session.add(users_request)
    db.session.commit()

    # Add the two UsersReqs

    user_request = UsersReqs(email=user_logged_in,
                             req_id=users_request.req_id,
                             requestor=True)

    requestee_request = UsersReqs(email=requestee,
                                  req_id=users_request.req_id,
                                  requestor=False)

    db.session.add(user_request)
    db.session.add(requestee_request)
    db.session.commit()

    return jsonify({"msg": "Success"}), 200


@requests.route('/respond', methods=['POST'])
@jwt_required
def respond():
    user_logged_in = get_jwt_identity()
    # print(user_logged_in)

    req_id = request.json.get('req_id', None)
    # print(req_id)
    response = request.json.get('response', None)

    # If the response is true -> complete the request
    if response:
        print("User approves request")

        # Send money
        req = Requests.query.filter_by(req_id=req_id).first()
        print(req.amount_req)

        loggedInReq = (UsersReqs.query.
                    filter(UsersReqs.req_id == req_id).
                    filter(UsersReqs.requestor == False).first())

        usersReq = (UsersReqs.query.
                       filter(UsersReqs.req_id == req_id).
                       filter(UsersReqs.requestor == True).first())

        print("Email of other person: " + str(usersReq.email))
        print("Email of person logged in: " + str(loggedInReq.email))

        send_money(user_logged_in, usersReq.email, req.amount_req)

        # Delete request from request table
        db.session.delete(req)

        # Delete the two usersReqs rows from the UsersReqs table
        db.session.delete(usersReq)
        db.session.delete(loggedInReq)

        db.session.commit()

    # if false delete response
    else:
        # Delete request from request table
        req = Requests.query.filter_by(req_id=req_id).first()
        usersReq = (UsersReqs.query.
                    filter(UsersReqs.req_id == req_id).
                    filter(UsersReqs.requestor == False).first())

        loggedInReq = (UsersReqs.query.
                       filter(UsersReqs.req_id == req_id).
                       filter(UsersReqs.requestor == True).first())

        db.session.delete(req)

        # Delete the two usersReqs rows from the UsersReqs table
        db.session.delete(usersReq)
        db.session.delete(loggedInReq)

        db.session.commit()

    return jsonify({"msg": "Success"}), 200
