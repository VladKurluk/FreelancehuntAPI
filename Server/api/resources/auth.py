from flask_restful import reqparse, abort, Resource
from flask_bcrypt import generate_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity
import datetime
from database import db
from api.models import User
from peewee import IntegrityError, DoesNotExist
from api.resources.errors import EmailAlreadyExistsError, UserDoesNotExist, UnauthorizedError, InternalServerError


def hash_password(pas):
    """
    Функция, которая хеширует пароль
    :param pas: Пароль введенный пользователем для хеширования, String
    :return: Хеш пароля, String
    """
    return generate_password_hash(pas).decode('utf8')


class AuthRegister(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help='You need to enter your name', required=True)
        parser.add_argument('email', type=str, help='You need to enter your e-mail address', required=True)
        parser.add_argument('password', type=str, help='You need to enter your password', required=True)

        args = parser.parse_args()

        name = args.get('name')
        email = args.get('email')
        password_hash = hash_password(args.get('password'))

        try:
            with db.atomic():
                # Создание юзера. Если Email уже существует в базе
                # будет вызвано исключение IntegrityError.
                User.create(name=name, email=email, password=password_hash)
            return {'message': 'Аккаунт успешно создан.'}, 201
        except IntegrityError:
            raise EmailAlreadyExistsError
        except Exception as e:
            raise InternalServerError

class AuthLogin(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, help='You need to enter your e-mail address', required=True)
        parser.add_argument('password', type=str, help='You need to enter your password', required=True)

        args = parser.parse_args()

        email = args.get('email')
        password = args.get('password')

        try:
            user = User.get(User.email == email)
            authorized = user.check_password(password)

            if not authorized:
                raise UnauthorizedError

            expires = datetime.timedelta(minutes=5)
            access_token = create_access_token(identity=str(user.id), expires_delta=expires)
            return {
                       'access_token': access_token,
                       'refresh_token': create_refresh_token(identity=str(user.id)),
                       'username': user.name
                   }, 200
        except DoesNotExist as e:
            raise UserDoesNotExist

class AuthRefreshToken(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        expires = datetime.timedelta(minutes=5)
        return {'access_token': create_access_token(identity=current_user, expires_delta=expires)}, 200

class AuthTestToken(Resource):
    @jwt_required
    def get(self):
        username = get_jwt_identity()
        return {'Auth': "Authorisation is ok"}, 200