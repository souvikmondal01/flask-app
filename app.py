from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()


@app.route('/')
def index():
    return jsonify(name="Souvik Mondal")


@app.route("/hello", methods=["GET"])
def hello():
    return jsonify(msg="hello world")


if __name__ == "__main__":
    app.run(debug=True)
