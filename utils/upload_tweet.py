import json
import random

def upload(api, musicOfDay):
    """Start by uploading the mp4 video, then add the description containing the day, title, artist, album, link, and date. 
    Finally, post the tweet, along with the description and media.
    
    Args:
        api : client Twitter
        musicOfDay (dict): all informations about music of day
    """
    media = api.media_upload('uploads/video.mp4')
        
    title = musicOfDay[0].title_short
    artist = musicOfDay[0].artist["name"]
    album = musicOfDay[0].album["title"]
    day = musicOfDay[1]
    link = musicOfDay[0].link
    date = musicOfDay[0].release_date

    with open('utils/data/sentences.json', "r") as file :
        file = json.load(file)

    sentence = random.choice(file)

    tweet = f"Day {day}\n\n🎵 Title : {title}\n👨‍🎤 Artist : {artist}\n🎸 Album : {album}\n🔗 Link : {link}\n📆 Date : {date}\n\n🤟 {sentence}\n#music #deezer"
    api.update_status(status=tweet, media_ids=[media.media_id])