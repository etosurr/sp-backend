from flask import request, jsonify
from flask_jwt_extended import create_access_token
from flask_bcrypt import Bcrypt
from app import app


bcrypt = Bcrypt(app)


@app.route('/register', methods=['POST'])
def register():
    first_name = request.get_json()['first_name']
    last_name = request.get_json()['last_name']
    email = request.get_json()['email']
    password = bcrypt.generate_password_hash(request.get_json()['password']).decode('utf-8')

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
    access_token = create_access_token(identity=(email, password))
    return jsonify({'result': access_token})
