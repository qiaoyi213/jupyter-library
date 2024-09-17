import sqlite3

from flask import current_app, g

DATABSE = "jupyter_library.db"


def init_db():
    if current_app:
        db = get_db()
        with current_app.open_resource("migrations/schema.sql", mode="r") as f:
            db.cursor().executescript(f.read())
        db.commit()


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABSE)
    return db
