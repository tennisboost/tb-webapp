from peewee import *
#from playhouse.postgres_ext import *

import psycopg2

db = PostgresqlDatabase('tboost', user='tomhill')

# Note models should be named the singular, not plural
class UserAccount(Model):
    email = CharField(unique=True)
    password = CharField() # This will be hashed by bcrypt or similar
    companyName = CharField()

    class Meta:
        database = db

class Comp(Model):
    # user = ForeignKeyField(rel_model=UserAccount, related_name='Comp') <-- for when we add in user functionality fully
    name = CharField()
    comp_type = CharField()
    singlesDoubles = CharField()
    # scores = hmmmm unfortunately only PostgreSQL provides ArrayField or JSONField functionality... hence we might have to switch to it.
    # I'm too tired to implement that right at this moment...
    # http://docs.peewee-orm.com/en/latest/peewee/playhouse.html#ArrayField
    #players = ArrayField(CharField)
    #scores = ArrayField(CharField)

    class Meta:
        database = db

    @classmethod
    def create_comp(cls, name, comp_type, singlesDoubles):
        cls.create(
            name = name,
            comp_type = comp_type,
            singlesDoubles = singlesDoubles
        )

def init():
    db.connect()
    db.create_tables([UserAccount, Comp], safe=True)
    print('=== BUILT MODELS ===')
    db.close()
