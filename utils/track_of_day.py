import random

from deezpy.playlist import Playlist
from deezpy.song import Track

list_tracks_passed = []

def get_trackOfDay():
    
    playlist = Playlist(9949516322)
    list_tracks = []
    
    for tracks in playlist.tracks["data"]:
        list_tracks.append(tracks["id"])

    tracks_for_today = random.choice(list_tracks)
    
    while tracks_for_today in list_tracks_passed:
        tracks_for_today = random.choice(list_tracks)
    
    list_tracks_passed.append(tracks_for_today)
    
    musicOfDay = Track(tracks_for_today)

    return musicOfDay, len(list_tracks_passed)