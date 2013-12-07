from echonest import *
from aoty import *

if __name__ == "__main__":
  x = EchoNest()

  create_tables()

  fname = '2013.txt'
  albums = [line.strip() for line in open(fname)]


  for album in albums:
    array = album.split(' - ')
    artist = array[0]
    title = array[1]
    failed = []

    print artist + ' - ' + title
    try:
      album = Album.select().where(Album.title == title).where(Album.artist == artist).get()
    except Album.DoesNotExist:
      album = Album.create(artist=artist, title=title)

    terms = x.terms(artist)

    if not terms:
      failed.append(artist + ' - ' + title)
      continue
    else:
      for term in terms:
        print term
        try:
          tag = Tag.select().where(Tag.name == term).get()
        except Tag.DoesNotExist:
          tag = Tag.create(name=term)

        try:
          at = AlbumTag.select().where(AlbumTag.album == album).where(AlbumTag.tag == tag).get()
        except AlbumTag.DoesNotExist:
          at = AlbumTag.create(album=album, tag=tag)


    print failed