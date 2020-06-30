from flask import Blueprint
from flask_restful import Api

from api.resources import auth
from api.resources.errors import errors


def create_resourses(app):
    # Start api/v1 Blueprint
    api_bp = Blueprint('api', __name__)
    api = Api(api_bp, errors=errors)

    api.add_resource(auth.AuthRegister, '/auth/register')
    api.add_resource(auth.AuthLogin, '/auth/login')
    api.add_resource(auth.AuthRefreshToken, '/auth/refresh_token')
    api.add_resource(auth.AuthTestToken, '/auth/protected')

    app.register_blueprint(api_bp, url_prefix="/api/v1")
    # End api/v1 Blueprint
