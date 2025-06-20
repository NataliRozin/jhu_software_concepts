"""
Application factory module.

This module defines the application factory function `create_app`, which
constructs and returns a Flask application instance. It also registers the
`pages` Blueprint from the `website` package.
"""

from flask import Flask
from website import pages

# Flask constructor
def create_app() -> Flask:
    """
    Create and configure a Flask application instance.

    This function initializes a Flask app, registers the `pages` Blueprint,
    and returns the app instance.

    Returns
    -------
    Flask
        A configured Flask application instance.
    """
    # Create a new Flask application instance
    app = Flask(__name__)

    # Register the 'pages' Blueprint with the app
    app.register_blueprint(pages.bp)

    return app
