from flask import Blueprint, jsonify, request
from flask_api.extensions import db
from flask_api.models import Users
# Remember to import JWT stuff for tokens and authentication


user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users', methods=['GET'])
def user_search():
    # if not request.is_json:
    #     return jsonify({"msg": "Missing JSON in request"}), 400


    #email = request.json.get('email', None)
    users = Users.query.all()

    user_list = []

    for i in users:
        list_item = {"first_name": i.first_name, "last_name": i.last_name, "email": i.email}
        # user_list.append("{" + f"first_name: {i.first_name}, last_name: {i.last_name}, email: {i.email}" + "}")
        user_list.append(list_item)
        #user_list.append(jsonify({f"first_name: {i.first_name}, last_name: {i.last_name}, email: {i.email}"}))
        #user_list.append("{""first_name: {i.first_name}, last_name: {i.last_name}, email: {i.email}" + "}")

    print(user_list)

    return jsonify(user_list), 200

@user_routes.route('/user/balance', methods=['GET'])
def user_balance():

    email = request.json.get('email', None)

    user = Users.query.filter_by(email=email).first()

    if user is None:
        return jsonify({"msg": "User doesn't exit"}), 400

    print(user.account_balance)
    
    return jsonify({"balance": user.account_balance}), 200