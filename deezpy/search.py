import requests
import json 

from deezpy.song import Track

BASE_URL = 'https://api.deezer.com/search?q='

class Search :
    """A self made Search Engine for the Deezer API
    """
    def __init__(self, query_string : str):
        """Return the result of a research with a querystring as argument

        Args:
            query_string (str): What you search
        """
        r = requests.get(f'{BASE_URL}{query_string}')
        r = r.json()
        
        for keys in dict(r):
            setattr(self, keys, r[keys])
            
        self.track = Track(int(self.data[0]['id']))