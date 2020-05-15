from flask import Blueprint
from flask_cors import CORS

# Blueprints need to be added to the file that constructs
# the application (ie __init__.py) to be used by the app
main = Blueprint('main', __name__)
CORS(main)

# A welcome message to test our server
@main.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"
