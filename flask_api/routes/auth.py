from flask import Blueprint, Flask, jsonify, request
from flask_api.extensions import db
from flask_api.models import Users

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=["GET", "POST"])
def register():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    email = request.json.get('email', None)
    #print(email)
    password = request.json.get('password', None)
    #print(password)
    first_name = request.json.get('first_name', None)
    #print(first_name)
    last_name = request.json.get('last_name', None)
    #print(last_name)

    user = Users(first_name=first_name, last_name=last_name, email=email, password=password)

    #dbuser = Users.query.filter_by(email=email).first()        

    if Users.query.filter_by(email=email).first():
        print('User already in the database')
        return jsonify("User already in the database")
    else:
        print(f"Adding  {user.first_name} to the DB!")        
        db.session.add(user)
        db.session.commit()

        return jsonify(email, password, first_name, last_name)
 

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    
    email = request.json.get('email', None)
    #print(email)
    password = request.json.get('password', None)
    #print(password)

    
    user = Users.query.filter_by(email=email).first()

    if user:
        if user.password == password:
            print("Logged in")

            return jsonify('Valid login')
        else:
            print("Password incorrect")
            
            return jsonify('Invalid Password')
        
    else:
        print("user not in db")

        return jsonify('Invalid Username')