# This file is used to create the tables in the database

import click
from flask.cli import with_appcontext

from .extensions import db
from .models import Users, Banks, Transactions

@click.command(name='create_tables')
@with_appcontext
def create_tables():
	db.create_all()