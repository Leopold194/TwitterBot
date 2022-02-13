import requests 
import json 

BASE_URL = 'https://api.deezer.com/playlist/'

class Playlist:
    """A class who represent a playlist in Deezer API
    """
    def __init__(self, id : int):
        """Create a Playlist with Deezer API and set url response at argument

        Args:
            id (int): The id of playlist
        """
        r = requests.get(f'{BASE_URL}{id}')
        r = r.json()
        
        for key in dict(r) :
            setattr(self, key, r[key])
            