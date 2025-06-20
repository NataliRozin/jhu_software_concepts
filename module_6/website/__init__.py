from flask import Flask
from website import pages

# Flask constructor
def create_app():
    # Create a new Flask application instance
    app = Flask(__name__)

    # Register the 'pages' Blueprint with the app
    app.register_blueprint(pages.bp)

    return app