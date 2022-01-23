import urllib.request

def download_audio(link : str) -> int :
    try : 
        data = urllib.request.urlretrieve(link, 'uploads/songOfDay.mp3')
        return 0
    except :
        return 1
    
def download_image(link : str) -> int :
    try :
        data = urllib.request.urlretrieve(link, 'uploads/coverOfDay.jpg')
        return 0
    except  :
        return 1