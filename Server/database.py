from peewee import *
import datetime

db = SqliteDatabase('parser_app.db', pragmas={
    'journal_mode': 'wal',
    'cache_size': -1 * 64000,  # 64MB
    'foreign_keys': 1,
    'ignore_check_constraints': 0,
    'synchronous': 0})

class User(Model):
    name = CharField()
    email = CharField()
    password = TextField()
    join_date = DateTimeField(default=datetime.datetime.now)

    def to_dict(self):
        return dict(id=self.id, email=self.email)

    class Meta:
        database = db
        table_name = "Users"


def create_tables():
    with db:
        db.drop_tables([User])
        db.create_tables([User])