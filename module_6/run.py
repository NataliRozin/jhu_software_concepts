"""
Entry point for the Flask web application.

This module initializes and runs the Flask app using the factory pattern.
It imports the `create_app` function from the `website` package, builds the
WSGI application object, and runs it when executed directly.

The application is set to run on host ``0.0.0.0`` and port ``8080``, with debug
mode enabled.

Usage:
    python <this_file>.py

Attributes
----------
app : Flask
    The Flask WSGI application instance created by the factory function.
"""

# an object of WSGI application
from website import create_app

# building the app
app = create_app()

if __name__ == "__main__":
    # run the application
    app.run(host="0.0.0.0", port=8000, debug=True)
