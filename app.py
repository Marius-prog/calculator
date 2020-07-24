from flask import Flask, render_template, request, make_response, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from functools import wraps
from flask_login import LoginManager, UserMixin, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = 'some secret'
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calculator.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
manager = LoginManager(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


@manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# def __repr__(self):
#     return


# def authorization(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         auth = request.authorization
#         if auth and auth.username == 'user' and auth.password == 'pass':
#             return f(*args, **kwargs)
#         return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required!"'})
#     return decorated


@app.route('/')
# @login_required
def index():
    return render_template('index.html')


@app.route('/send', methods=['POST'])
# @authorization
def send():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']

        if not num1 or not num2:
            error_message = 'All Form Fields Required..'
            return render_template('page_not_found.html', error_message=error_message)
        elif num2 == 0:
            error_zero = 'Not aloud to divide by 0 !!'
            return render_template('zero.html', error_zero=error_zero)

    if operation == 'add':
        sum = float(num1) + float(num2)
        return render_template('index.html', sum=sum, num1=num1, num2=num2, operation=operation)


    elif operation == 'subtract':
        sum = float(num1) - float(num2)
        return render_template('index.html', sum=sum, num1=num1, num2=num2, operation=operation)


    elif operation == 'multiply':
        sum = float(num1) * float(num2)
        return render_template('index.html', sum=sum, num1=num1, num2=num2, operation=operation)


    elif operation == 'divide':
        try:
            sum = float(num1) / float(num2)
        except ZeroDivisionError:
            zero_message = 'Not aloud division by 0 !!'
            flash('Not aloud division by 0 !!')
            return render_template('zero.html', zero_message=zero_message)
    return render_template('index.html', sum=sum, num1=num1, num2=num2, operation=operation)


# @app.route('/calculations', methods=['POST', 'GET'])
# def calc():
#     if request.method == "POST":
#         user_name = request.form('name')
#         new_user = User(name=user_name)
#
#         try:
#             db.session.add(new_user)
#             db.session.commit()
#             return redirect('/calculations')
#         except:
#             return "error to adding user"
#     else:
#         users = User.query.order_by(User.date_created)
#         return render_template('calculations.html', users=users)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    login = request.form.get('login')
    password = request.form.get('password')

    if login and password:
        user = User.query.filter_by(login=login).first()
        if check_password_hash(user.password, password):
            load_user(user)

            next_page = request.args.get('next')

            redirect(next_page)
        else:
            flash('Login or password not correct !!')
    else:
        flash('Please fill login and password fields !!')
        return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    login = request.form.get('login')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if request.method == 'POST':
        if not (login or password or password2):
            flash('Please fill all fields !!')
        elif password != password2:
            flash('Password are not equal !!')
        else:
            hash_pass = generate_password_hash(password)
            new_user = User(login=login, password=password, hash_pass=hash_pass)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login_page'))

    return render_template('register.html')


# @app.route('/logout', methods=['GET', 'POST'])
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('hello_world'))


@app.after_request
def redirect_to_signing(response):
    if response.status_code == 401:
        return redirect(url_for('login_page') + '?next='+request.url)
    return response



@app.errorhandler(404)
def error(error):
    return render_template('index.html', error=error), 404


if __name__ == "__main__":
    app.run(debug=True)
