from datetime import datetime

from flask import Flask, render_template, request

from app.commands import add, subtract, multiply, divide
from app.validations import validate_number
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calculator.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.id


@app.route("/")
def index():
    return render_template("app.html")


@app.route("/first", methods=["POST"])
def post_first_number():
    print("pirmas")
    number = request.form["number"]
    validate_number(number)


@app.route("/second", methods=["POST"])
def post_second_number():
    print("antras")
    number = request.form["number"]
    validate_number(number)


@app.route("/operation", methods=["POST"])
def post_operation_number():
    print("operation")
    operation = request.form["operation"]


@app.route("/calculate")
def get_result():
    operation = request.form.get["operation"]
    if operation == "add":
        result = add(1, 5)
    elif operation == "subtract":
        result = subtract(1, 2)
    elif operation == "multiply":
        result = multiply(1, 2)
    else:
        result = divide(1, 2)


@app.errorhandler(404)
def error(error):
    return render_template("index.html", error=error), 404


if __name__ == "__main__":
    app.run(debug=True, port=2000)
