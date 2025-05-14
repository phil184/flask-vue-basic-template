from flask import Blueprint, jsonify, request
from api import lm
from .models import User
from flask_login import login_user, logout_user, login_required, current_user

base_view = Blueprint('base_view', __name__)


@base_view.route('/')
def index():
    return jsonify("API response")


@base_view.route('/api/login', methods=['POST', 'GET'])
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
    
@login_required
@base_view.route('/api/logout', methods=['POST', 'GET'])
def logout():
    logout_user()
    
    return jsonify({
        'message' : 'Logout'
    })
    
    
@login_required
@base_view.route('/api/dashboard', methods=['GET', 'POST'])
def dashboard():
    return jsonify({
        'message': f'Welcome, {current_user.username}'
    })


# User-loader
@lm.user_loader
def load_user(user_id):
    return User.query.get(user_id)