import tweepy as tw
import os
import time
import random
import urllib.request

from bs4 import BeautifulSoup
from deezpy.playlist import Playlist
from deezpy.song import Track
from utils.track_of_day import get_trackOfDay
import utils.dowload as dl
import utils.video_generator as vg

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
except:
    print("Bot has a problem")

run = True
while run == True:

    musicOfDay = get_trackOfDay()
    link_video = musicOfDay[0].link
    link_cover = musicOfDay[0].album["cover_big"]

    sock = urllib.request.urlopen(link_video)
    htmlPage = sock.read()
    sock.close()
    soup = BeautifulSoup(htmlPage)
    meta_list = soup.find_all('meta')
    for i in meta_list:
        try:
            if i["property"] == "og:audio":
                audio = dl.download_audio(i["content"])
        except:
            pass

    image = dl.download_image(link_cover)

    def convert_mp3_to_shortmp3():
        os.system("ffmpeg -i uploads/songOfDay.mp3 -ss 0 -t 29 uploads/songOfDay_short.mp3")
        return True

    if audio == 0 and image == 0:
        convert_mp3 = convert_mp3_to_shortmp3()
    else:
        print("Error with audio or image")
        run = False

    while convert_mp3 != True:
        pass

    vg.make_video()

    def convert_avi_to_mp4():
        os.popen("ffmpeg -i uploads/video.avi -vf scale=-2:480,format=yuv420p -c:v libx264 -profile:v high -preset slow -b:v 500k -maxrate 500k -bufsize 1000k -threads 0 -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 uploads/video.mp4")

    convert_avi_to_mp4()
    ready = False

    while ready != True:
        try:
            with open('uploads/video.mp4'): pass
            ready = True
        except IOError:
            pass

    time.sleep(5)

    media = api.media_upload('uploads/video.mp4')
    title = musicOfDay[0].title_short
    artist = musicOfDay[0].artist["name"]
    album = musicOfDay[0].album["title"]
    day = musicOfDay[1]
    tweet = f"Day {day}\n\nTitle : {title}\nArtiste : {artist}\nAlbum : {album}"
    post = api.update_status(status=tweet, media_ids=[media.media_id])
    os.remove('uploads/video.mp4'); os.remove('uploads/video.avi'); os.remove('uploads/coverOfDay.jpg'); os.remove('uploads/songOfDay.mp3'); os.remove('uploads/songOfDay_short.mp3')
    run = False