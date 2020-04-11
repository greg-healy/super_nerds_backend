import time
from flask import Blueprint, Flask, request, jsonify
from flask_cors import CORS
from flask_api.extensions import db
from flask_api.models import Users, Banks, Transactions

# Blueprints need to be added to the file that constructs
# the application (ie __init__.py) to be used by the app
main = Blueprint('main', __name__)
CORS(main)

@main.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)

@main.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

# A welcome message to test our server
@main.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

@main.route('/time')
def get_current_time():
    return {'time': time.time()}