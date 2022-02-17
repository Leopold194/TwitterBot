import urllib.request
import os

from bs4 import BeautifulSoup

import utils.dowload as dl

def convert_mp3_to_shortmp3():
        os.system("ffmpeg -i uploads/songOfDay.mp3 -ss 0 -t 29 uploads/songOfDay_short.mp3")

def get_audio(link_video):
    
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
    
    return dl.download_image(link_image)