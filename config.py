import os

class Config:
    debug = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://maryam:maryam@localhost/pitch'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG =True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}