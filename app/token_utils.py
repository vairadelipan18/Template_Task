from flask import request, jsonify, current_app
import jwt
from functools import wraps
from app.models import User 

def token_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        token = None
        
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]

        if not token:
            return jsonify({'message': 'Token is missing!'}), 403

        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])

            current_user = User.objects(id=data['user_id']).first()
            
            if not current_user:
                return jsonify({'message': 'User not found!'}), 403

        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 403

        return f(current_user, *args, **kwargs)

    return wrap
