from flask import Blueprint, jsonify, request
from flask_api.models import Users
from flask_jwt_extended import jwt_required, get_jwt_identity


user_routes = Blueprint('user_routes', __name__)


@user_routes.route('/users', methods=['GET'])
@jwt_required
def user_search():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    print(request)

    users = Users.query.all()

    user_list = []

    for i in users:
        list_item = {"first_name": i.first_name,
                     "last_name": i.last_name,
                     "email": i.email}

        user_list.append(list_item)

    print(user_list)

    return jsonify(user_list), 200


@user_routes.route('/user/balance', methods=['GET'])
@jwt_required
def user_balance():

    email = get_jwt_identity()

    user = Users.query.filter_by(email=email).first()

    if user is None:
        return jsonify({"msg": "User doesn't exit"}), 400

    print(user.account_balance)

    return jsonify({"balance": user.account_balance}), 200
