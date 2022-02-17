def upload(api, musicOfDay):

    media = api.media_upload('uploads/video.mp4')
        
    title = musicOfDay[0].title_short
    artist = musicOfDay[0].artist["name"]
    album = musicOfDay[0].album["title"]
    day = musicOfDay[1]
    link = musicOfDay[0].link
    date = musicOfDay[0].release_date

    tweet = f"Day {day}\n\nTitle : {title}\nArtist : {artist}\nAlbum : {album}\nLink : {link}\nDate : {date}\n"
    api.update_status(status=tweet, media_ids=[media.media_id])