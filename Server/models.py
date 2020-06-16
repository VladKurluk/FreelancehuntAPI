from peewee import *

db = SqliteDatabase('parser_app.db', pragmas={
    'journal_mode': 'wal',
    'cache_size': -1 * 64000,  # 64MB
    'foreign_keys': 1,
    'ignore_check_constraints': 0,
    'synchronous': 0})

class User(Model):
    name = CharField()
    login = CharField()

    class Meta:
        database = db
        table_name = "Users"


def create_tables():
    with db:
        db.create_tables([User])