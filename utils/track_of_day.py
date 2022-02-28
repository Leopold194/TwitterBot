import random
import json

from deezpy.playlist import Playlist
from deezpy.song import Track

def get_trackOfDay(exception = False):

    """Checks which titles have already been played, and retrieves a title that has never been played in the playlist.
    Then attribute to musicOfDay the Track object which contains all the information of the selected music
    
    Returns:
        musicOfDay (Track): A Track object
        len(file) (int): The number of titles already passed.    
    """
    with open('utils/data/musics_passed.json', "r") as file :
        file = json.load(file)

    playlist = Playlist(9949516322)
    list_tracks = []
    
    for tracks in playlist.tracks["data"]:
        list_tracks.append(tracks["id"])

    tracks_for_today = random.choice(list_tracks)
    
    while tracks_for_today in file:
        tracks_for_today = random.choice(list_tracks)
    
    file.append(tracks_for_today)
    
    musicOfDay = Track(tracks_for_today)

    with open('utils/data/musics_passed.json', "w") as writer : 
        json.dump(file, writer)

    return (musicOfDay, len(file))