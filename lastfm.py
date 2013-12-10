import requests
import yaml
import urllib
import os.path
import re
import pdb


class LastFM:
  """
  Handle API requests to Last.fm API
  """

  def __init__(self):
    self.base_uri = 'http://ws.audioscrobbler.com/2.0/'
    self.api_key = yaml.load(open("api.yml", 'r'))['lastfm']['api_key']

  def get_album_info(self, album):
    params = {'method': 'album.getInfo', 'api_key': self.api_key, 'autocorrect': 1,
              'artist': album.artist, 'album': album.title, 'format': 'json' }
    response = requests.get(self.base_uri, params=params).json()
    if(response['album']['image']):
      for image in response['album']['image']:
        if(image['size'] == 'extralarge'):
          filename = 'images/' +  re.sub('[^\w\s-]', '', album.artist + '-' + album.title).strip().lower() + '.png'
          if not os.path.isfile('site/' + filename):
            urllib.urlretrieve(image['#text'], 'site/' + filename)
          album.image = filename
    if response['album']['listeners']:
      album.listeners = response['album']['listeners']
    if response['album']['url']:
      album.lastfm_url = response['album']['url']
    album.save()

  def get_top_tags(self, album, tag_whitelist):
    terms = set()
    params = {'method': 'album.getTopTags', 'api_key': self.api_key, 'autocorrect': 1,
              'artist': album.artist, 'album': album.title, 'format': 'json' }
    response = requests.get(self.base_uri, params=params).json()
    if response.get('toptags', {}).get('tag') and isinstance(response['toptags']['tag'], (list, tuple)):
      for tag in response['toptags']['tag']:
        item_norm = re.sub('\s+', '-', tag['name'])
        # I dont love this but it's annoying me
        if item_norm == 'rnb':
            item_norm = 'r&b'
        if(tag['count'] > 5 and item_norm in tag_whitelist):
          terms.add(item_norm)
    return terms