# Импорт класса HTTPException от которого наследуються все
# пользовательские классы исключения
from werkzeug.exceptions import HTTPException


class InternalServerError(HTTPException):
    pass

class SchemaValidationError(HTTPException):
    pass

class EmailAlreadyExistsError(HTTPException):
    pass

class UserDoesNotExist(HTTPException):
    pass

class UnauthorizedError(HTTPException):
    pass


errors = {
    "InternalServerError": {
        "message": "Хьюстон, хьюстон! У нас проблемы!",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "EmailAlreadyExistsError": {
         "message": "Пользователь с таким Email уже существует.",
         "status": 400
     },
    "UserDoesNotExist": {
        "message": "Пользователя не существует.",
        "status": 401
    },
     "UnauthorizedError": {
         "message": "Неверный пароль.",
         "status": 401
     }
}
