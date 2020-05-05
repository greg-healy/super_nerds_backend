from flask import Flask
from flask_cors import CORS

# Database functionality
from .extensions import db
from .commands import create_tables

# Blueprints/routes
from .routes.main import main
from .routes.auth import auth

def create_app(config_file='settings.py'):
    app = Flask(__name__)
    CORS(app)

    # Setup the Flask-JWT-Extended extension 
    app.config['JWT_SECRET_KEY'] = 'super-nerds-secret'  # Change this!
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

    # Running `flask create_tables` will create the tables for us
    # Must be run again if more tables are created/changed
    # On Heroku must also run `flask create_tables` in console
    app.cli.add_command(create_tables)

    return app
