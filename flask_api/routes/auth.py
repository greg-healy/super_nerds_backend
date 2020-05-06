from flask import Blueprint, Flask, jsonify, request
from flask_api.extensions import db
from flask_api.models import Users
from flask_jwt_extended import (
    jwt_required, JWTManager, create_access_token,
    get_jwt_identity
)

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=["GET", "POST"])
def register():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    email = request.json.get('email', None)
    if not email:
        return jsonify({"msg": "Missing email"}), 400
    # print(email)

    password = request.json.get('password', None)
    if not password:
        return jsonify({"msg": "Missing password"}), 400
    # print(password)

    first_name = request.json.get('first_name', None)
    if not first_name:
        return jsonify({"msg": "Missing first name"}), 400
    # print(first_name)

    last_name = request.json.get('last_name', None)
    if not last_name:
        return jsonify({"msg": "Missing last name"}), 400
    # print(last_name)

    user = Users(first_name=first_name,
                 last_name=last_name,
                 email=email,
                 password=password)

    if Users.query.filter_by(email=email).first():
        # print('User already in the database')
        return jsonify({"msg": "User already in DB"}), 400
    else:
        # print(f"Adding  {user.first_name} to the DB!")
        db.session.add(user)
        db.session.commit()
        # return jsonify(email, password, first_name, last_name)
        return jsonify(first_name=first_name,
                       last_name=last_name,
                       email=email,
                       password=password), 200


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    email = request.json.get('email', None)
    if not email:
        return jsonify({"msg": "Missing email"}), 400
    # print(email)
    password = request.json.get('password', None)
    if not password:
        return jsonify({"msg": "Missing password"}), 400
    # print(password)

    user = Users.query.filter_by(email=email).first()

    if user:
        if user.password == password:
            # print("Logged in")
            # return jsonify('Valid login')
            access_token = create_access_token(identity=user.email)
            return jsonify({"access_token": access_token,
                            "status": "success",
                            "error_msg": ""})
        else:
            #  print("Password incorrect")
            #  return jsonify('Invalid Password')
            return jsonify({"msg": "Invalid password"}), 401
    else:
        # print("user not in db")
        return jsonify({"msg": "User not in DB"}), 400
