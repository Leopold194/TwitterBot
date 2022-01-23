import requests
import json 

from deezpy.song import Track

BASE_URL = 'https://api.deezer.com/search?q='

class Search :
    
    def __init__(self, query_string : str):
        r = requests.get(f'{BASE_URL}{query_string}')
        r = r.json()
        
        for keys in dict(r):
            setattr(self, keys, r[keys])
            
        self.track = Track(int(self.data[0]['id']))