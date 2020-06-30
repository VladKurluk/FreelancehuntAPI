"""
Здесь собираеться приложение которое импортируеться в run.py для запуска.
"""

from flask import Flask
from database import create_tables
from config import config
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from api import create_resourses

def create_app(env):
    app = Flask(__name__)

    create_tables()

    app.config.from_object(config[env])

    CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
    CORS(app, resources={r"/parser/*": {"origins": "*"}})
    CORS(app, resources={r"/auth/v1/*": {"origins": "*"}})

    create_resourses(app)

    from freelance_api.api import fh_api
    app.register_blueprint(fh_api, url_prefix="/api/v1")

    # from site_parser.main import parser
    # app.register_blueprint(parser, url_prefix="/parser")

    bcrypt = Bcrypt(app)
    jwt = JWTManager(app)

    return app