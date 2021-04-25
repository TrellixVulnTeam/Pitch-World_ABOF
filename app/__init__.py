from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config_options

# from config import Config
app = Flask(__name__)

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)



def create_app(config_name):
    app.config.from_object(config_options[config_name])
  
    return app
