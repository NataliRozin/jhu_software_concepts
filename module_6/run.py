# an object of WSGI application
from website import create_app

# building the app
app = create_app()

if __name__ == "__main__":
    # run the application
    app.run(host="0.0.0.0", port=8000, debug=True)