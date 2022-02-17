import tweepy as tw
import os
import random

from deezpy.playlist import Playlist
from deezpy.song import Track
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

    playlist = Playlist(9949516322)
    list_tracks = []
    list_tracks_passed = []
    for tracks in playlist.tracks["data"]:
        list_tracks.append(tracks["id"])

    tracks_for_today = random.choice(list_tracks)
    while tracks_for_today in list_tracks_passed:
        tracks_for_today = random.choice(list_tracks)
    list_tracks_passed.append(tracks_for_today)
    print(tracks_for_today)

    link_video = Track(tracks_for_today).link
    link_cover = Track(tracks_for_today).album["cover_small"]

    print(link_video)

    audio = dl.download_audio(link_video)
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
        return True

    convert = convert_avi_to_mp4()

    while convert != True:
        pass

    #media = api.media_upload('uploads/video.mp4')
    tweet = "Test"
    #post = api.update_status(status=tweet, media_ids=[media.media_id])
    run = False