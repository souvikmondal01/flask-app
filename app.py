from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


# DB_URL = "postgresql+psycopg2://postgres:12345@localhost:5432/crudApp"
DB_URL = "postgresql://crudapp_9e03_user:t8Lb0Uoh1nfgBTSNtoWt4pe5nr8oDF7T@dpg-cf9tcbun6mpv49fcjmb0-a.oregon-postgres.render.com/crudapp_9e03"
SECRET_KEY = "yoursecretkey"

app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False
app.secret_key = SECRET_KEY
db.init_app(app)
print("DB Initialized Successfully")


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)


@app.route('/')
def index():
    return jsonify(name="Souvik Mondal")


@app.route("/hello", methods=["GET"])
def hello():
    return jsonify(msg="hello world")


@app.route("/signup", methods=["POST", "GET"])
def signup():
    name = request.form["name"]
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]

    new_user = User(name=name, username=username,
                    email=email,password=password)
    db.session.add(new_user)
    # db.drop_all()
    db.create_all()
    db.session.commit()
    return jsonify(msg="user added successfully")


if __name__ == "__main__":
    app.run(debug=True)
