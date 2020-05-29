from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

# Database functionality
from .extensions import db
from .commands import create_tables

# Blueprints/routes
from .routes.main import main
from .routes.auth import auth
from .routes.bank import bank_routes
from .routes.user import user_routes
from .routes.requests import requests
from .routes.transactions import transactions
from .routes.debugging import debugging


def create_app(config_file='settings.py'):
    app = Flask(__name__)
    CORS(app)

    # Setup the Flask-JWT-Extended extension
    app.config['JWT_SECRET_KEY'] = 'super-nerds-secret'  # Change this!
    app.config['JWT_HEADER_NAME'] = 'Authorization'
    app.config['JWT_HEADER_TYPE'] = ''
    jwt = JWTManager(app)

    # Takes environment variables from the .env file and assigns them
    # to values for use by the app
    app.config.from_pyfile(config_file)

    # Instantiating the database
    db.init_app(app)

    # Brings the functionality of the routes defined in routes folder using
    # the "main" and "auth" blueprints and applies them to the app defined
    # in here

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(bank_routes)
    app.register_blueprint(user_routes)
    app.register_blueprint(requests)
    app.register_blueprint(transactions)
    app.register_blueprint(debugging)

    # Running `flask create_tables` will create the tables for us
    # Must be run again if more tables are created/changed
    # On Heroku must also run `flask create_tables` in console
    app.cli.add_command(create_tables)

    return app
