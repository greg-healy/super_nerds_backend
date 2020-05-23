"""
File: auth.py
Description: Aquires data from /register & /login routes, validates and
appropriately stores / sends back user data
"""

from flask import Blueprint, jsonify, request
from flask_api.extensions import db
from flask_api.models import Users
from flask_jwt_extended import create_access_token

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=["GET", "POST"])
def register():
    """
    Sets the User email, password, first name and last name.

    Args:
        None

    Returns:
        JSON object and status code: a descriptive message with a corresponding
        HTTP response status code.
    """

    email = request.json.get('email', None)

    password = request.json.get('password', None)

    first_name = request.json.get('first_name', None)

    last_name = request.json.get('last_name', None)

    potential_user = Users(first_name=first_name,
                           last_name=last_name,
                           email=email,
                           password=password,
                           account_balance=0.0)

    user_in_db = Users.query.filter_by(email=email).first()

    if user_in_db:
        return jsonify({"msg": "User already in DB"}), 409

    else:
        db.session.add(potential_user)
        db.session.commit()

        return jsonify({"msg": "Registration Success!"}), 201


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Validates email/password and and logs the user in using Flask JWT

    Args:
        None

    Returns:
        JSON object and status code: a descriptive message with a corresponding
        HTTP response status code.

        access_token: a JWT object (only if validation successful)
    """

    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    email = request.json.get('email', None)
    if not email:
        return jsonify({"msg": "Missing email"}), 400

    password = request.json.get('password', None)
    if not password:
        return jsonify({"msg": "Missing password"}), 400

    user = Users.query.filter_by(email=email).first()

    if user:
        if user.password == password:
            access_token = create_access_token(identity=user.email)
            print(access_token)
            return jsonify({"access_token": access_token,
                            "status": "success",
                            "error_msg": ""})
        else:
            return jsonify({"msg": "Invalid password"}), 401
    else:
        return jsonify({"msg": "User not in DB"}), 400
