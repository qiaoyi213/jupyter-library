from flask import Blueprint, jsonify, request

from . import db
from .models import User

bp = Blueprint("main", __name__)


@bp.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([user.username for user in users])
