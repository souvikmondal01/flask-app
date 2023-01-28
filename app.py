from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify(name="Souvik Mondal")


@app.route("/hello", methods=["GET"])
def hello():
    return jsonify(msg="hello world")


if __name__ == "__main__":
    app.run(debug=True)
