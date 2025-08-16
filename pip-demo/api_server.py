from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return {"message": "Hello from pip/venv!"}


if __name__ == "__main__":
    app.run(port=5000)
    app.run(port=5000)
