from flask import Flask 
from config import config_options

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bootstap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
   
    db.init_app(app)
    bootstap.init_app(app)

def create_app(config_name):
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    
    return app
