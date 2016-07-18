import sqlite3
from app import app, g
from app.model.db_service import db_connection


def init_db():
    """Initializes the database."""
    with app.app_context():
        db = db_connection.get_db()
        with app.open_resource('database/schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')


initdb_command()
