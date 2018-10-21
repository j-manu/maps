from peewee import *
from playhouse.postgres_ext import *

database = PostgresqlDatabase('maps', **{})

class BaseModel(Model):
    class Meta:
        database = database

class Data(BaseModel):
    departure_time = DateTimeField()
    distance_in_metres = IntegerField()
    end_address = TextField()
    full_result = BinaryJSONField(null=True)
    mode = TextField()
    start_address = TextField()
    steps = BinaryJSONField()
    time_in_seconds = BigIntegerField()
    transit_mode = TextField(null=True)

    class Meta:
        table_name = 'data'

