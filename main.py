import tweepy as tw
import os
import time

from datetime import datetime

from utils.upload_tweet import upload
from utils.get_functional_video import create_functional_video
from utils.track_of_day import get_trackOfDay
from utils.get_audio_image import get_audio, get_image

consumer_key = "Y0w1V5Fx08E9YVwb8yeEQZkTJ"
consumer_secret = "tbXHOsf1DFyhxzr2YePJzIz3BXWkIJ2GHk0Zx8YsRnNkfnyhGq"

access_token = "1494014284761907203-fDqNtiqF7sJ8S5Xy5hdcnxSXcMVUl0"
access_token_secret = "nhcarTONHrDHEWvgbyw1G7uhSq2feubhICba4M3eDrRBT"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)

try:
    api.verify_credentials()
    print("Bot is online")
    connect = True
except:
    print("Bot has a problem")

while connect:

    actually_time = datetime.now()
    print(actually_time)

    if actually_time.hour == 10 and (actually_time.minute == 0 or actually_time.minute == 1):

        try:

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