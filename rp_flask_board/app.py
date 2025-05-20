from flask import Flask

def create_app():
    app = Flask(__name__)

    return app

@app.route("/")
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)