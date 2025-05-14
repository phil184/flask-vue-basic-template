import os

"""
Basic Class-Config, for advanced Setups visit: 
https://flask.palletsprojects.com/en/stable/config/

"""

class Config(object):
	"""
	Configuration base
	"""
	DEBUG = False
	TESTING = False
	SQLALCHEMY_DATABASE_URI = 'sqlite:///user.db'
	SECRET_KEY = 'superSecret'
	CSRF_ENABLED = True 
 	
	

class ProductionConfig(Config):
    
	SQLALCHEMY_DATABASE_URI = ''
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
	DEBUG = True

class TestingConfig(Config):
	TESTING = True
    