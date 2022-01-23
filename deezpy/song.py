import requests
import json 

BASE_URL = 'https://api.deezer.com/track/'

class Track :
    
    def __init__(self, id : int) :
        r = requests.get(url = f"{BASE_URL}{str(id)}")
        r = r.json()
        
        for keys in dict(r) :
            setattr(self, keys, r[keys])
        