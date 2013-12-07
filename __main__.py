from echonest import *
from aoty import *

if __name__ == "__main__":
  echonest = EchoNest()

  create_tables()

  fname = '2013.txt'
  albums = [line.strip() for line in open(fname)]
  failed = []


  for album in albums:
    array = album.split(' - ')
    artist = array[0]
    title = array[1]

    print artist + ' - ' + title
    album = get_or_create_album(artist, title)

    terms = echonest.get_terms(artist)

    if not terms:
      failed.append(artist + ' - ' + title)
      continue
    else:
      for term in terms:
        print term
        tag = get_or_create_tag(term)
        get_or_create_album_tag(album, tag)

  print failed