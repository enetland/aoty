#!/usr/bin/python
from peewee import *

database = SqliteDatabase('aoty.db')

class SqliteModel(Model):
    class Meta:
        database = database

class Album(SqliteModel):
  title = CharField()
  artist = CharField()
  image = CharField(null=True)
  listeners = IntegerField(null=True)
  rank = IntegerField(null=True)

  def tags(self):
    return [tag.name for tag in Tag.select().join(AlbumTag).where(AlbumTag.album == self)]

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

def get_or_create_album(artist, title):
  try:
    album = Album.select().where(Album.title == title).where(Album.artist == artist).get()
  except Album.DoesNotExist:
    album = Album.create(artist=artist, title=title)
  return album

def get_or_create_tag(name):
  try:
    tag = Tag.select().where(Tag.name == name).get()
  except Tag.DoesNotExist:
    tag = Tag.create(name=name)
  return tag

def get_or_create_album_tag(album, tag):
  try:
    at = AlbumTag.select().where(AlbumTag.album == album).where(AlbumTag.tag == tag).get()
  except AlbumTag.DoesNotExist:
    at = AlbumTag.create(album=album, tag=tag)
  return at

def popular_tags():
  return Tag.raw('select * from tag t where (select count(*) from albumtag a where a.tag_id = t.id) > 1 order by (select count(*) from albumtag a where a.tag_id = t.id) DESC')

#import sqlite3
#conn = sqlite3.connect('test.db')

