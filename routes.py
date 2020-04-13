from flask import request, jsonify
from flask_jwt_extended import create_access_token
from flask_bcrypt import Bcrypt
from app import app
from database import db, User, List, Portfolio, Stock

bcrypt = Bcrypt(app)


@app.route('/register', methods=['POST'])
def register():
    first_name = request.get_json()['first_name']
    last_name = request.get_json()['last_name']
    email = request.get_json()['email']
    password = bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')

    user = User(first_name=first_name, last_name=last_name,
                email=email, password_hash=password)
    db.session.add(user)
    db.session.commit()

    result = {
        'first_name': first_name,
        'last name': last_name,
        'email': email,
        'password': password
    }
    return jsonify({'result': result})


@app.route('/login', methods=['POST'])
def login():
    email = request.get_json()['email']
    password = request.get_json()['password']
    user = User.query.filter_by(email=email).first()
    rv = user.password_hash
    if bcrypt.check_password_hash(rv, password):
        access_token = create_access_token(identity=(email, password))
        return jsonify({'result': access_token})
    else:
        result = jsonify({"error": "invalid password"})
        return result
