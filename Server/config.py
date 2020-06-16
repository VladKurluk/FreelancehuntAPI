'''
Классы для конфигурации приложения в разных средах (develoment/production)
'''

class Config(object):
    DEBUG = True
    TESTING = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///parser_app.db'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SECRET_KEY = "S0m3S3cr3tK3y"

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}