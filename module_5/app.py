"""
app.py
======

This module defines and runs a Flask web application that loads applicant data
from a local JSON file into a PostgreSQL database and queries various statistics
to display on a web page.
"""

import json
import psycopg
from flask import Flask, render_template, abort
from db.load_data import run_loader
from db.query_data import Query

# Flask constructor
def create_app():
    """
    Initializes and configures the Flask application.

    This function:
      - Creates the Flask app instance.
      - Sets up the main route (`/`) that triggers data loading and querying.
      - Returns the configured Flask app object.

    :returns: The configured Flask application instance.
    :rtype: Flask
    """

    # Create a new Flask application instance
    app = Flask(__name__)

    # Load data into the database when the app starts (only once)
    try:
        run_loader() # Ensure the table is created and loaded with data
    except (FileNotFoundError, json.JSONDecodeError, psycopg.Error, OSError) as e:
        print(f"Error running data loader on startup: {e}")  # Print known loader-related errors

    @app. route('/')
    def index() :
        """
        Root route handler for the web application.

        This function:
          - Calls :func:`run_loader` to create and populate the database table, if empty.
          - Uses the :class:`~db.query_data.Query` class to query statistics from the database.
          - Passes the resulting data to the `index.html` template for rendering.

        :returns: Rendered HTML page with summary statistics.
        :rtype: str
        """
        try:
            # Initialize the Query object to access predefined queries
            q = Query()

            # Execute queries and store results in a dictionary
            results = {
                "fall25_count": q.count_fall25_entries(),
                "intl_percent": q.international_percentage(),
                "intl_avgs": q.average_scores_international_fall25(),
                "american_avg_gpa": q.average_gpa_american_fall25(),
                "accepted_count": q.accepted_fall25_percentage(),
                "accepted_avg_gpa": q.average_gpa_accepted_fall25(),
                "jhu_cs_masters_count": q.count_jhu_cs_masters(),
            }

            # Render the template with the statistics rsults
            return render_template('index.html', results=results)

        except psycopg.Error as e:
            # Catch known database errors from psycopg
            print(f"Database error while querying: {e}")
            return abort(500, description="Internal Server Error")
        except RuntimeError as e:
            # Catch basic runtime issues (e.g., if template rendering fails)
            print(f"Runtime error during request: {e}")
            return abort(500, description="Internal Server Error")

    return app

# Main execution block
if __name__ == "__main__":
    flask_app = create_app()

    # run the application
    flask_app.run(host="0.0.0.0", port=8000, debug=True)
