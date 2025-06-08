from flask import Flask, render_template
from DB.load_data import run_loader
from DB.query_data import Query

# Flask constructor
def create_app():
    # Create a new Flask application instance
    app = Flask(__name__)

    @app. route('/')
    def index() :
        run_loader()
        
        # Collect data from Query methods
        q = Query()

        results = {
            "fall25_count": q.count_fall25_entries(),
            "intl_percent": q.international_percentage(),
            "intl_avgs": q.average_scores_international_fall25(),
            "american_avg_gpa": q.average_gpa_american_fall25(),
            "accepted_count": q.count_accepted_fall25(),
            "accepted_avg_gpa": q.average_gpa_accepted_fall25(),
            "jhu_cs_masters_count": q.count_jhu_cs_masters(),
        }

        return render_template('index.html', results=results)

    return app

if __name__ == "__main__":
    app = create_app()

    # run the application
    app.run(host="0.0.0.0", port=8000, debug=True)