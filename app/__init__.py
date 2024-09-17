from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()


def create_app():
    app = Flask("Jupyter-Library")
    app.config.from_object("config")
    db.init_app(app)

    with app.app_context():
        from .database import init_db

        init_db()
        db.create_all()

    from app.auth import auth_blueprint

    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    @app.route("/")
    def hello():
        return "Hello"

    @app.route("/test_db")
    def test_db():
        return db.inspect(db.engine).get_table_names()
        try:
            result = db.session.execute(text("SELECT 1"))
            return (
                "Database connected successfully!"
                if result
                else "Database connection failed."
            )
        except Exception as e:
            return f"Database connection failed: {str(e)}"

    return app
