from flask import current_app
from flask_login import UserMixin

from app import db
from app.utils.bcrypt_util import check_password, encode_password


class User(UserMixin, db.Model):
    __tablename__ = "user"
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password):
        self.password_hash = encode_password(password)

    def check_password(self, password):
        return check_password(password, self.password_hash)
