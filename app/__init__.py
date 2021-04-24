from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config_options

# from config import Config
app = Flask(__name__)

#Initializing flask extension
bootstrap = Bootstrap()
db = SQLAlchemy()

#
def create_app(config_name):
    return app
