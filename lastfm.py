
import requests
import yaml
import pdb


class EchoNest:
    """
    Handle API requests to Last.fm API
    """
    def __init__(self):
      self.base_uri = 'http://ws.audioscrobbler.com/2.0/'
      self.api_key = yaml.load(open("api.yml", 'r'))['lastfm']['api_key']

    def get_album_info(self, artist, album):
      base_url = self.base_uri
      params = {'method': 'album.getInfo', 'api_key': self.api_key,
                'artist': artist, 'album': album, 'format': 'json' }
      response = requests.get(base_url, params=params).json()
      pdb.set_trace()
      if(response['album']['image']):

      else:
        print response



