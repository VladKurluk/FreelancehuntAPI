'''
Здесь собираеться приложение которое импортируеться в run.py для запуска.
'''

from flask import Flask
from config import config
from flask_cors import CORS

def create_app(env):
    app = Flask(__name__)
    app.config.from_object(config[env])
    cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

    from freelance_api.api import api
    app.register_blueprint(api, url_prefix="/api/v1")

    from site_parser.main import parser
    app.register_blueprint(parser, url_prefix="/parser")

    return app