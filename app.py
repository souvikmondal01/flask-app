from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()


@app.route('/')
def index():
    return jsonify(name="Souvik Mondal")


@app.route("/hello", methods=["GET"])
def hello():
    return jsonify(msg="hello world")


@app.route("/signup", methods=["POST","GET"])
def signup():
    name = request.form["name"]
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]

    user_dict = {"name": name, "username": username, "email": email}

    return user_dict


if __name__ == "__main__":
    app.run(debug=True)
