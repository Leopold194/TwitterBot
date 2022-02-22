import tweepy as tw
import os
import time

from datetime import datetime

from utils.upload_tweet import upload
from utils.get_functional_video import create_functional_video
from utils.track_of_day import get_trackOfDay
from utils.get_audio_image import get_audio, get_image

consumer_key = "Write here your consumer key"
consumer_secret = "Write here your consumer secret key"

access_token = "Write here your access token"
access_token_secret = "Write here your access token secret"

"""Used to connect to the Twitter client
"""
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)

"""Check if the keys are correct.
"""
try:
    api.verify_credentials()
    print("Bot is online")
    connect = True
except:
    print("Bot has a problem")

while connect:

    """Check if it's time to post the tweet, especially here 6am
    """
    actually_time = datetime.now()
    if actually_time.hour == 6 and (actually_time.minute == 0 or actually_time.minute == 1):

        try:

            """Start by recovering the sound of the day, then isolate the link and the cover of this music
            Then create mp4 video which will contain audio and cover.
            Finally, post the tweet, and delete the files that are no longer needed.
            """
            musicOfDay = get_trackOfDay()
            link_video = musicOfDay[0].link
            link_cover = musicOfDay[0].album["cover_xl"]

            get_audio(link_video); get_image(link_cover)
            
            create_functional_video()

            time.sleep(5)

            upload(api, musicOfDay)

            os.remove('uploads/video.mp4'); os.remove('uploads/video.avi'); os.remove('uploads/coverOfDay.jpg'); os.remove('uploads/songOfDay.mp3'); os.remove('uploads/songOfDay_short.mp3')

        except:

            print(f"Error {actually_time}")
        
    else:

        time.sleep(30)
