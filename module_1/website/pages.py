# Import necessary Flask functions
from flask import Blueprint, render_template

# Create a Blueprint named "pages"
bp = Blueprint("pages", __name__)

# Define a route for the home page ("/")
@bp.route("/")
def home():
    return render_template("pages/home.html")

# Define a route for the contact page ("/contact")
@bp.route("/contact")
# Render the home.html template from the "pages" folder
def contact():
    # Render the contact.html template from the "pages" folder
    return render_template("pages/contact.html")

# Define a route for the projects page ("/projects")
@bp.route("/projects")
def projects():
    # Render the projects.html template from the "pages" folder
    return render_template("pages/projects.html")