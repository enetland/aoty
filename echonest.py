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
      self.api_key = yaml.load(open("api.yml", 'r'))['api_key']

    def terms(self, artist):
      base_url = self.base_uri + 'artist/terms'
      artist_formatted = re.sub('\s+', '+', artist.lower())
      params = { 'api_key': self.api_key, 'name': artist_formatted }
      response = requests.get(base_url, params=params).json()
      terms = []
      if(response['response']['status']['code'] == 0):
        for item in itertools.islice(response['response']['terms'], 10):
          terms.append(item['name'])
      elif(response['response']['status']['code'] == 5):
      else:
        print response
      return terms



