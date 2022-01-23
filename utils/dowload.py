import urllib.request

def download_audio(link : str) -> int :
    try : 
        data = urllib.request.urlretrieve(link, 'uploads/songOfDay.mp3')
        return 1
    except :
        return 0
    
    