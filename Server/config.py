"""
Классы для конфигурации приложения в разных средах (development/production)
"""
from os import environ

class Config(object):
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = environ.get('JWT_SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///parser_app.db'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SECRET_KEY = "S0m3S3cr3tK3y"

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}