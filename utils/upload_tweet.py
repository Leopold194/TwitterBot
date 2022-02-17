def upload(api, musicOfDay):
    """Start by uploading the mp4 video, then add the description containing the day, title, artist, album, link, and date. 
    Finally, post the tweet, along with the description and media.
    
    Args:
        api : client Twitter
        musicOfDay (dict): all informations about music of day
    """
    media = api.media_upload('uploads/video.mp4')
        
    title = musicOfDay[0].title_short
    artist = musicOfDay[0].artist["name"]
    album = musicOfDay[0].album["title"]
    day = musicOfDay[1]
    link = musicOfDay[0].link
    date = musicOfDay[0].release_date

    tweet = f"Day {day}\n\nTitle : {title}\nArtist : {artist}\nAlbum : {album}\nLink : {link}\nDate : {date}\n\n#music #deezer"
    api.update_status(status=tweet, media_ids=[media.media_id])