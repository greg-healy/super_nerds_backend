from flask import Blueprint
from flask_api.extensions import db
from flask_api.models import Users

auth = Blueprint('auth', __name__)

@auth.route('/register')
def register():
	pass

@auth.route('/login')
def login():
	pass
