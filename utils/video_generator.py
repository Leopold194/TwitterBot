import os

def make_video(image_link = 'uploads/coverOfDay.jpg', audio_link = 'uploads/songOfDay.mp3') :
    os.system(f'ffmpeg -loop 1 -y -i {image_link} -i {audio_link} -shortest -acodec copy -vcodec mjpeg uploads/videoOfDay.avi')
    