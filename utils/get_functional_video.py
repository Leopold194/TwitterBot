import os
import time

import utils.video_generator as vg

def create_functional_video():
    """First create the video in .avi, then convert it to .mp4 to be readable by twitter.
    Then does a loop, to wait for the end of the conversion.
    """
    vg.make_video()

    time.sleep(60)
			
    os.popen("ffmpeg -i uploads/video.avi -vf scale=-2:480,format=yuv420p -c:v libx264 -profile:v high -preset slow -b:v 500k -maxrate 500k -bufsize 1000k -threads 0 -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 uploads/video.mp4")