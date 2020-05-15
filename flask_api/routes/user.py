from flask import Blueprint, jsonify, request
from flask_api.extensions import db
# Remember to import JWT stuff for tokens and authentication


user_routes = Blueprint('user_routes', __name__)
