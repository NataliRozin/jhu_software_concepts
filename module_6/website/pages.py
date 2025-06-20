"""
Pages Blueprint module.

This module defines the `pages` Blueprint, which handles routes for the main
pages of the website including home, contact, and projects.

Routes:
- `/`          : Home page
- `/contact`   : Contact page
- `/projects`  : Projects page
"""

from flask import Blueprint, render_template, Response  # Import Response for type hinting

# Create a Blueprint named "pages"
bp = Blueprint("pages", __name__)

@bp.route("/")
def home() -> Response:
    """
    Render the home page.

    Returns
    -------
    Response
        Rendered HTML template for the home page.
    """
    return render_template("pages/home.html")

@bp.route("/contact")
def contact() -> Response:
    """
    Render the contact page.

    Returns
    -------
    Response
        Rendered HTML template for the contact page.
    """
    return render_template("pages/contact.html")

@bp.route("/projects")
def projects() -> Response:
    """
    Render the projects page.

    Returns
    -------
    Response
        Rendered HTML template for the projects page.
    """
    return render_template("pages/projects.html")
