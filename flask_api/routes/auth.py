# auth.py will acquire data from the forms provide on the
# /register and /login routes and appropriate action
# base on data in the database

from flask import Blueprint, jsonify, request
from flask_api.extensions import db
from flask_api.models import Users
from flask_jwt_extended import create_access_token

auth = Blueprint('auth', __name__)

# register() will set variables email, password, first_name,
# last_name with values entered into the form. These individual
# values are components of the User object and table. If the user
# does not exists in the database, they are added, otherwise an
# error notification is sent back.


@auth.route('/register', methods=["GET", "POST"])
def register():

    email = request.json.get('email', None)

    password = request.json.get('password', None)

    first_name = request.json.get('first_name', None)

    last_name = request.json.get('last_name', None)

    user = Users(first_name=first_name,
                 last_name=last_name,
                 email=email,
                 password=password)

    if Users.query.filter_by(email=email).first():
        return jsonify({"msg": "User already in DB"}), 409
    else:
        db.session.add(user)
        db.session.commit()

        return jsonify({"msg": "Registration Success!"}), 201

# The login() function will acquire form data and place it into
# the fields email and password. If the user has a registered account
# and the password is correct, an access token is created and sent
# back. The token will be used for user identification and page
# navigation. The logic will otherwise return appropriate messages
# if bad data is provided.


@auth.route('/login', methods=['GET', 'POST'])
def login():
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
            return jsonify({"access_token": access_token,
                            "status": "success",
                            "error_msg": ""})
        else:
            return jsonify({"msg": "Invalid password"}), 401
    else:
        return jsonify({"msg": "User not in DB"}), 400
