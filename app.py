import sqlite3

from flask import Flask
from flask_login import LoginManager

app = Flask("Jupyter-Library")
app.config.from_object("config")
config = app.config
app.secret_key = config.get("SECRET_KEY")
login_manager = LoginManager()
login_manager.init_app(app)


@app.route("/Ping")
def Ping():
    return "Pong"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
