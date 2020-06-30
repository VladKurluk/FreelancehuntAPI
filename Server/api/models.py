from peewee import *
from database import db
import datetime
from flask_bcrypt import check_password_hash

class User(Model):
    """
    Модель данных Пользователя
    """
    name = CharField()
    email = CharField(unique=True)
    password = CharField()
    join_date = DateTimeField(default=datetime.datetime.now)

    def check_password(self, password):
        """
        Функция идентификации введенного пользователем пароля с хешом пароля хранящимся в БД.
        :param password: Пароль, String
        :return: Результат сравнения хеш-пароля, Boolean
        """
        return check_password_hash(self.password, password)

    class Meta:
        database = db
        table_name = "Users"