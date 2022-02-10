import mysql.connector
from peewee import MySQLDatabase, Model, TextField, AutoField, CharField


cretedb = mysql.connector.connect(
    host="sqlvnx",
    user="user",
    password="abc123")
mycur = cretedb.cursor()
try:
    mycur.execute("CREATE DATABASE news")
except Exception as ex:
    print(str(ex))

db = MySQLDatabase(
    'news',
    user='user',
    password='abc123',
    host='sqlvnx')


class BaseModel(Model):
    class Meta:
        database = db


class Data(BaseModel):
    id = AutoField()
    tieude = CharField()
    mota = TextField()
    noidung = TextField()
    uri = CharField()


class Users(BaseModel):
    id = AutoField()
    email = CharField()
    password = CharField()


db.create_tables([Users, Data])
