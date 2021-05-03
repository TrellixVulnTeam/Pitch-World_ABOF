import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    SQLALCHEMY_TRACK_MODIFICATIONS = False


    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    # simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://ccgnlwqkmtyhaj:aec3addb6933801aa7e16fd06135ded5d3ae443d55914f55f06d84f2ca90aa92@ec2-54-160-96-70.compute-1.amazonaws.com:5432/d8k1e767hq3b5j?sslmode=require"


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://maryam:1234@localhost/pitch'
    DEBUG = True
    ENV = 'development'

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://maryam:1234@localhost/pitch'



config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}
