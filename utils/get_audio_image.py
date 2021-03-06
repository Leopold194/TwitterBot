import urllib.request
import os

from bs4 import BeautifulSoup

import utils.dowload as dl

def convert_mp3_to_shortmp3():
    
    """Reduced the time of the audio to 29 seconds so that it is possible to post it on Twitter.
    """
    os.popen("ffmpeg -i uploads/songOfDay.mp3 -ss 0 -t 29 uploads/short_audio.mp3")

def get_audio(link_video):
    
    """Start by getting the audio link from the music link query.
    Minimize it using the function above, then download the audio.
    """
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

    convert_mp3_to_shortmp3()
    
def get_image(link_image):
    
    """Dowload the cover
    """
    dl.download_image(link_image)