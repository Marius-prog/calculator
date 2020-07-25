from flask import Flask, render_template, request, make_response, redirect, flash, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from flask_login import LoginManager, UserMixin, login_required, logout_user
import jwt
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
# app.secret_key = 'some secret'
app.config['SECRET_KEY'] = 'Th1s1ss3cr3t'
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calculator.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.id


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send', methods=['POST', 'GET'])
def send():
    users = []
    results = {}
    if request.method == 'POST':
        name = request.form['name']
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']

        if not num1 or not num2:
            error_message = 'All Form Fields Required..'
            flash('All Form Fields Required..')
            return render_template('page_not_found.html', error_message=error_message)
        elif num2 == 0:
            error_zero = 'Division by 0 not allowed !!'
            return render_template('zero.html', error_zero=error_zero)

    if operation == 'add':
        sum = float(num1) + float(num2)
        return render_template('index.html', sum=sum, num1=num1, num2=num2, operation=operation, name=name)


    elif operation == 'subtract':
        sum = float(num1) - float(num2)
        return render_template('index.html', sum=sum, num1=num1, num2=num2, operation=operation, name=name)


    elif operation == 'multiply':
        sum = float(num1) * float(num2)
        return render_template('index.html', sum=sum, num1=num1, num2=num2, operation=operation, name=name)


    elif operation == 'divide':
        try:
            sum = float(num1) / float(num2)
        except ZeroDivisionError:
            zero_message = 'Division by 0 not allowed !!'
            flash('Division by 0 not allowed !!')
            return render_template('zero.html', zero_message=zero_message)
    return render_template('index.html', sum=sum, num1=num1, num2=num2, operation=operation, name=name)


@app.after_request
def redirect_to_signing(response):
    if response.status_code == 401:
        return redirect(url_for('login_page') + '?next=' + request.url)
    return response


@app.errorhandler(404)
def error(error):
    return render_template('index.html', error=error), 404


if __name__ == "__main__":
    app.run(debug=True)
