from flask import request, jsonify,current_app
import jwt
import datetime
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash


def register_user():
    data = request.get_json()


    new_user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        password=data['password']
    )
    
    if User.objects(email=data['email']):
        return jsonify({'message': 'Email already exists!'}), 400
    new_user.save()

    return jsonify({'message': 'User created successfully!'}), 201

def login_user():
    data = request.get_json()

    user = User.objects(email=data.get('email')).first()
    if not user:
        return jsonify({'message': 'Invalid credentials!'}), 401
    if user.password != data.get('password'):
        return jsonify({'message': 'Wrong password!'}), 401

    token = jwt.encode({
        'user_id': str(user.id),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, current_app.config['SECRET_KEY'], algorithm="HS256")

    return jsonify({
        'token': token,
        'message': 'Login Successfully'
    }), 200