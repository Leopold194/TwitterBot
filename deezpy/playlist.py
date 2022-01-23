import requests 
import json 

BASE_URL = 'https://api.deezer.com/playlist/'

class Playlist:
    
    def __init__(self, id : int):
        r = requests.get(f'{BASE_URL}{id}')
        r = r.json()
        
        for key in dict(r) :
            setattr(self, key, r[key])
            