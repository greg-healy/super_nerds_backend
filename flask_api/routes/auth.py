from flask import Blueprint
from flask_api.extensions import db
from flask_api.models import Users

auth = Blueprint('auth', __name__)


@auth.route('/register')
def register():
    return "<h1>Register is working!</h1>"


@auth.route('/login')
def login():
    return "<h1>Login is working!</h1>"
