#!/usr/bin/python
from peewee import *

database = SqliteDatabase('aoty.db')

class SqliteModel(Model):
    class Meta:
        database = database

class Album(SqliteModel):
  title = CharField()
  artist = CharField()

class Tag(SqliteModel):
  name = CharField()

class AlbumTag(SqliteModel):
  album = ForeignKeyField(Album)
  tag = ForeignKeyField(Tag)

def create_tables():
  Album.create_table(True)
  Tag.create_table(True)
  AlbumTag.create_table(True)

database.connect()


#import sqlite3
#conn = sqlite3.connect('test.db')

