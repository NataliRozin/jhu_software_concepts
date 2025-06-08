from flask import Flask, render_template
from DB.connection import get_db_connection

# Flask constructor
def create_app():
    # Create a new Flask application instance
    app = Flask(__name__)

    @app. route('/')
    def index() :
        conn = get_db_connection()
        cur  = conn.cursor()
        cur.execute('SELECT * FROM applicants; ')
        applicants = cur.fetchall ()
        cur.close()
        conn.close()
        return render_template('index.html', applicants=applicants)

    return app

if __name__ == "__main__":
    app = create_app()

    # run the application
    app.run(host="0.0.0.0", port=8000, debug=True)