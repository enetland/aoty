import requests
import yaml
import urllib
import os.path
import re


class LastFM:
    """
    Handle API requests to Last.fm API
    """
    def __init__(self):
      self.base_uri = 'http://ws.audioscrobbler.com/2.0/'
      self.api_key = yaml.load(open("api.yml", 'r'))['lastfm']['api_key']

    def get_album_info(self, album):
      base_url = self.base_uri
      params = {'method': 'album.getInfo', 'api_key': self.api_key, 'autocorrect': 1,
                'artist': album.artist, 'album': album.title, 'format': 'json' }
      response = requests.get(base_url, params=params).json()
      if(response['album']['image']):
        for image in response['album']['image']:
          if(image['size'] == 'extralarge'):
            filename = 'images/' +  re.sub('[^\w\s-]', '', album.artist + '-' + album.title).strip().lower() + '.png'
            if not os.path.isfile('site/' + filename):
              urllib.urlretrieve(image['#text'], 'site/' + filename)
            album.image = filename
        album.listeners = response['album']['listeners']
        album.lastfm_url = response['album']['url']
        album.save()
      else:
        print response



