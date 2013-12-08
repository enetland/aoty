from echonest import *
from lastfm import *
from aoty import *
import os

import generate_site

if __name__ == "__main__":
  echonest = EchoNest()
  lastfm = LastFM()

  create_tables()

  fname = '2013.txt'
  albums = [line.strip() for line in open(fname)]
  failed = []
  rank = 1
  if not os.path.exists('site/images'):
    os.makedirs('site/images')


  for album in albums:
    array = album.split(' - ')
    artist = array[0]
    title = array[1]

    print artist + ' - ' + title
    album = get_or_create_album(artist, title)
    album.rank = rank
    album.save()
    rank += 1
    if album.image and AlbumTag.select().join(Album).where(Album.title == title).first():
      continue
    lastfm.get_album_info(album)

    terms = echonest.get_terms(artist)

    if not terms:
      failed.append(artist + ' - ' + title)
      continue
    else:
      for term in terms:
        print term
        tag = get_or_create_tag(term)
        get_or_create_album_tag(album, tag)
  generate_site.run('site/index.html')