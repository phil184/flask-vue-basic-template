from flask import Flask
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import LoginManager

# Extensions

db = SQLAlchemy()
lm = LoginManager()


def create_app():
    app = Flask(__name__)
    
    '''
    ATTENTION => ALLOWS CROSS-ORIGIN REQUESTS on ALL routes, from ANY domain,
    protocol etc.
    '''
    CORS(app, supports_credentials=True, resources={r'/*': {'origins': '*'}})

    
    # Basic Class-based config
    #app.config.from_object('api.config.ProductionConfig')
    app.config.from_object('api.config.DevelopmentConfig')
    #app.config.from_object('api.config.TestingConfig')
    
    
    # Init LoginManager
    
    
    # Init SqlAlchemy
    db.init_app(app)
    lm.init_app(app)
    lm.login_view = 'base_view.login'
    
    # Register Blueprints
    registerBlueprints(app)
    
    
    from .models import User
    # Database path
    db_path = Path(app.instance_path) / "user.db"
    with app.app_context():
        if not db_path.exists():
            db.create_all()
            # Create User
            # TODO: hashing
            username = str(input("Please enter username: "))
            password = str(input("Please enter password: "))
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            print(f"Database created with user: {user.username}" )
    
    return app

def registerBlueprints(app):
    from .views import base_view
    app.register_blueprint(base_view)
    
    # imports for testing blueprints ...
    