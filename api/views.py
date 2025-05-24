from flask import Blueprint, jsonify, request
from api import lm
from .models import User
from flask_login import login_user, logout_user, login_required, current_user

base_view = Blueprint('base_view', __name__)


@base_view.route('/')
def index():
    print(current_user)
    return jsonify("API response")

@base_view.route('/api/user')
@login_required
def abfrage():
    users = User.query.all()
    user_list = []
    for user in users:
        user_list.append({
            "id": user.id,
            "username": user.username,
        })

    print(user_list)
    return jsonify(user_list), 200


@base_view.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username') 
    password = data.get('password')
    user = User.query.filter_by(username=username).first()

    if user and user.password == password:
        login_user(user)
        
        return jsonify({
            "message" : "Login success"
        }), 200

    return jsonify({
        "message" : "Login failed"
    }), 400
    

@base_view.route('/api/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    
    return jsonify({
        'message' : 'Logout'
    }), 200
    
    
@base_view.route('/api/auth', methods=['GET'])
def authUser():
    if current_user.is_authenticated:
        return jsonify({
            'username': current_user.username
        }), 200
    else:
        return jsonify({
            'message' : 'Failed'
        }), 400
        

@lm.unauthorized_handler
def unauthorized():
    return jsonify({'error': 'Unauthorized'}), 401


# User-loader
@lm.user_loader
def load_user(user_id):
    return User.query.get(user_id)