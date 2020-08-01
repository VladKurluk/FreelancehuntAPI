from peewee import SqliteDatabase

db = SqliteDatabase('parser_app.db', pragmas={
    'journal_mode': 'wal',
    'cache_size': -1 * 64000,  # 64MB
    'foreign_keys': 1,
    'ignore_check_constraints': 0,
    'synchronous': 0})

from api.models import User

def create_tables():
    with db:
        # db.drop_tables([User], safe=True)
        db.create_tables([User], safe=True)
