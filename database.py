import sqlite3

from flask import g

DATABSE = "jupyter_library.db"


def init_db():
    conn = sqlite3.connect(DATABSE)
    c = conn.cursor()
    c.execute()
    conn.commit()
    conn.close()


def get_db():
    db = getter(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABSE)
    return db
