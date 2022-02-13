import urllib.request

def download_audio(link : str) -> int :
    """Download an audio from a weblink

    Args:
        link (str): Source of audio

    Returns:
        int: Result of operation 
    """
    try : 
        data = urllib.request.urlretrieve(link, 'uploads/songOfDay.mp3')
        return 0
    except :
        return 1
    
def download_image(link : str) -> int :
    """Download an image from a weblink

    Args:
        link (str): Source of image

    Returns:
        int: Result of operation
    """
    try :
        data = urllib.request.urlretrieve(link, 'uploads/coverOfDay.jpg')
        return 0
    except  :
        return 1