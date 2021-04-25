from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

from config import config_options

# from config import Config
app = Flask(__name__)

#Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile("config.py")

#Initializing flask extension
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

#
def create_app(config_name):
    return app
