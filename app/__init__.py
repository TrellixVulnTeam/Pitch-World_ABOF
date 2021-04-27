from flask import Flask 
from config import config_options
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bootstap = Bootstrap()
mail = Mail()

photos = UploadSet('photos',IMAGES)
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])

    #configure UploadSet
    configure_uploads(app,photos) 
   
    db.init_app(app)
    bootstap.init_app(app)
    mail.init_app(app)

def create_app(config_name):
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    
    return app
