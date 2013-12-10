import requests
import yaml
import re
import itertools

class EchoNest:
    """
    Handle API requests to EchoNest API
    """

    def __init__(self):
      self.base_uri = 'http://developer.echonest.com/api/v4/'
      self.api_key = yaml.load(open("api.yml", 'r'))['echonest']['api_key']

    def get_terms(self, artist, tag_whitelist):
      base_url = self.base_uri + 'artist/terms'
      artist_formatted = re.sub('\s+', '+', artist.lower())
      params = { 'api_key': self.api_key, 'name': artist_formatted }
      response = requests.get(base_url, params=params).json()
      terms = set()
      if(response['response']['status']['code'] == 0):
        for item in itertools.islice(response['response']['terms'], 10):
          item_norm = re.sub('\s+', '-', item['name'])
          # I dont love this but it's annoying me
          if item_norm == 'rnb':
              item_norm = 'r&b'
          if(item['weight'] > 0.7 and item_norm in tag_whitelist):
            terms.add(item_norm)
      else:
        print response
        print artist_formatted
      return terms



