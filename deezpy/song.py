import requests
import json 

BASE_URL = 'https://api.deezer.com/track/'

class Track :
    """A class who represents a specific track with it informations 
    """
    def __init__(self, id : int) :
        """Transform a web query as a class

        Args:
            id (int): ID of the song
        """
        r = requests.get(url = f"{BASE_URL}{str(id)}")
        r = r.json()
        
        for keys in dict(r) :
            setattr(self, keys, r[keys])
        