import os

import utils.video_generator as vg

def create_functional_video():
    vg.make_video()

    os.popen("ffmpeg -i uploads/video.avi -vf scale=-2:480,format=yuv420p -c:v libx264 -profile:v high -preset slow -b:v 500k -maxrate 500k -bufsize 1000k -threads 0 -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 uploads/video.mp4")

    ready = False

    while ready != True:
        try:
            with open('uploads/video.mp4'): pass
            ready = True
        except IOError:
            pass


