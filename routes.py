from flask import request, jsonify, redirect
from flask_jwt_extended import create_access_token
from flask_bcrypt import Bcrypt
from app import app
from database import db, User, List, Portfolio, Stock
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

bcrypt = Bcrypt(app)


@app.route('/register', methods=['POST'])
def register():
    first_name = request.get_json()['first_name']
    last_name = request.get_json()['last_name']
    email = request.get_json()['email']
    password = bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')

    user = User(first_name=first_name, last_name=last_name, email=email, password_hash=password)
    db.session.add(user)
    db.session.commit()

    result = {
        'first_name': first_name,
        'last name': last_name,
        'email': email,
        'password': password
    }
    return jsonify({'result': result})


@app.route('/login', methods=['GET', 'POST'])
def login():
    email = request.get_json()['email']
    password = request.get_json()['password']
    user = User.query.filter_by(email=email).first()
    rv = user.password_hash
    if bcrypt.check_password_hash(rv, password):
        access_token = create_access_token(identity={'first_name': user.first_name, 'last_name': user.last_name,
                                                     'email': email})
        return jsonify({"result": access_token})


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@app.route('/')
@login_required
def index():
    return 'Hello world'

