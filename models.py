from peewee import *

db = SqliteDatabase('test.db')

# Note models should be named the singular, not plural
class UserAccount(Model):
    email = CharField(unique=True)
    password = CharField() # This will be hashed by bcrypt or similar

class Comp(Model):
    # user = ForeignKeyField(rel_model=UserAccount, related_name='Comp') <-- for when we add in user functionality fully
    name = CharField()
    comp_type = CharField()
    singlesDoubles = CharField()
    # scores = hmmmm unfortunately only PostgreSQL provides ArrayField or JSONField functionality... hence we might have to switch to it.
    # I'm too tired to implement that right at this moment...
    # http://docs.peewee-orm.com/en/latest/peewee/playhouse.html#ArrayField
    # players = arrayField probs
