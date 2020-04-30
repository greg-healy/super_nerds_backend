# This file is used to create the tables in the database

import click  # Library that Flask uses for command line functionality
from flask.cli import with_appcontext  # lets commands use app config

from .extensions import db
from .models import Users, Banks, Transactions


@click.command(name='create_tables')  # defines the command
@with_appcontext
def create_tables():  # whatever you want to execute when you run the command
    db.create_all()
