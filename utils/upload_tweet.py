import json
import random
import time
<<<<<<< HEAD
import os
=======
>>>>>>> origin/main

def upload(api, musicOfDay, exception = False):
    """Start by uploading the mp4 video, then add the description containing the day, title, artist, album, link, and date. 
    Finally, post the tweet, along with the description and media.
    
    Args:
        api : client Twitter
        musicOfDay (dict): all informations about music of day
    """
    time.sleep(150)
	
    media = api.media_upload(filename='uploads/video.mp4')
    
    with open('utils/data/sentences.json', "r") as file :
        file = json.load(file)

    sentence = random.choice(file)

    title = musicOfDay[0].title_short
    artist = musicOfDay[0].artist["name"]
    album = musicOfDay[0].album["title"]
    link = musicOfDay[0].link
    date = musicOfDay[0].release_date
    day = musicOfDay[1]
<<<<<<< HEAD
    hashtag_artist = artist.replace(" ", "").replace("-", "").replace(",", "").replace(".", "")
    hashtag_title = title.replace(" ", "").replace("-", "").replace(",", "").replace(".", "")
    
    tweet = f"Day {day}\n\nšµ Title : {title}\nšØāš¤ Artist : {artist}\nšø Album : {album}\nš Link : {link}\nš Date : {date}\n\nš¤ {sentence}\n#music #deezer #{hashtag_artist} #{hashtag_title}"
    post = api.update_status(status=tweet, media_ids=[media.media_id])

    time.sleep(30)

    while os.listdir('uploads') != []:
    	for filename in os.listdir('uploads'):
            os.remove('uploads/' + filename)

=======

    tweet = f"Day {day}\n\nšµ Title : {title}\nšØāš¤ Artist : {artist}\nšø Album : {album}\nš Link : {link}\nš Date : {date}\n\nš¤ {sentence}\n#music #deezer"
   
    post = api.update_status(status=tweet, media_ids=[media.media_id])
>>>>>>> origin/main
    return 1