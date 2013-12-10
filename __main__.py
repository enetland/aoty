from echonest import *
from lastfm import *
from aoty import *
import os

import generate_site

if __name__ == "__main__":

  tag_whitelist = {'rock', 'pop', 'electronic', 'funk', 'house', 'disco',
                    'acoustic', 'ambient', 'blues', 'classical', 'experimental',
                    'hip-hop', 'rap', 'folk',
                    'punk', 'rnb', 'r&b', 'soul', 'idm', 'instrumental', 'lo-fi',
                    'psychadelic', 'garage-rock', 'noise', 'drone', 'country'}

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

    if not album.image or not album.lastfm_url or not album.listeners:
      lastfm.get_album_info(album)

    if not album.tags():
      terms = set()
      terms |= echonest.get_terms(artist, tag_whitelist)
      terms |= lastfm.get_top_tags(album, tag_whitelist)

      for term in terms:
        tag = get_or_create_tag(term)
        get_or_create_album_tag(album, tag)

  generate_site.run('site/index.html')