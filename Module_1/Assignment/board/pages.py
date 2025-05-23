from flask import Blueprint

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return "Hello, Home!"

@bp.route("/contact")
def contact():
    return "email + linkedin"

@bp.route("/projects")
def projects():
    return "my projects"