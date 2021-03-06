from main import db
from flask import Blueprint
import os

db_commands = Blueprint("db-custom", __name__)


@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    print("Tables deleted")