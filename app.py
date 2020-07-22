from flask import Flask, render_template, request, make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from functools import wraps


app = Flask(__name__)
# app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calculator.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

def __repr__(self):
    return 


def authorization(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'user1' and auth.password == 'pass':
            return f(*args, **kwargs)
        return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required!"'})

    return decorated


@app.route('/')
@authorization
def index():
    return render_template('index.html')


@app.route('/send', methods=['POST'])
@authorization
def send():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']

        if not num1 or not num2:
            error_message = 'All Form Fields Required..'
            return render_template('page_not_found.html',
                                   error_message=error_message,
                                   num1=num1,
                                   num2=num2,
                                   operation=operation)

    if operation == 'add':
        sum = float(num1) + float(num2)
        return render_template('index.html', sum=sum)


    elif operation == 'subtract':
        sum = float(num1) - float(num2)
        return render_template('index.html', sum=sum)


    elif operation == 'multiply':
        sum = float(num1) * float(num2)
        return render_template('index.html', sum=sum)


    elif operation == 'divide':
        sum = float(num1) / float(num2)
        return render_template('index.html', sum=sum)


@app.errorhandler(404)
def error(error):
    return render_template('index.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
