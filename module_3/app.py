"""
app.py

This module defines and runs a Flask web application that loads applicant data from a local JSON file
into a PostgreSQL database and queries various statistics to display on a web page.

"""

from flask import Flask, render_template
from DB.load_data import run_loader
from DB.query_data import Query

# Flask constructor
def create_app():
    """
    This function initializes the Flask application, sets up the main route, and prepares the app to run.
    It uses a data loader to ensure the database has data, then executes SQL queries to fetch and display
    statistical insights from the data.

    Returns:
        app (Flask): The configured Flask application instance.
    """

    # Create a new Flask application instance
    app = Flask(__name__)

    @app. route('/')
    def index() :
        """
        This function:
        1. Calls `run_loader()` to create the table (if does not exist) and load
           applicants data from a JSON file into the PostgreSQL database,
           only if the table is empty.
        2. Instantiates a Query object to retrieve various statistics about the data.
        3. Passes the results to the 'index.html' template for rendering.

        Returns:
            Rendered HTML page with data statistics.
        """

        # Ensure the table is created and loaded with data
        run_loader()
        
        # Query database for summary statistics
        q = Query()

        results = {
            "fall25_count": q.count_fall25_entries(),
            "intl_percent": q.international_percentage(),
            "intl_avgs": q.average_scores_international_fall25(),
            "american_avg_gpa": q.average_gpa_american_fall25(),
            "accepted_count": q.accepted_fall25_percentage(),
            "accepted_avg_gpa": q.average_gpa_accepted_fall25(),
            "jhu_cs_masters_count": q.count_jhu_cs_masters(),
        }

        return render_template('index.html', results=results)

    return app

if __name__ == "__main__":
    app = create_app()

    # run the application
    app.run(host="0.0.0.0", port=8000, debug=True)