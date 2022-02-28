import tweepy as tw
import os
import time
import smtplib, ssl

from keep_alive import keep_alive
from datetime import datetime

from utils.upload_tweet import upload
from utils.get_functional_video import create_functional_video
from utils.track_of_day import get_trackOfDay
from utils.get_audio_image import get_audio, get_image

consumer_key = "YOUR CONSUMER KEY"
consumer_secret = "YOUR CONSUMER KEY SECRET"

access_token = "YOUR ACCESS TOKEN"
access_token_secret = "YOUR ACCESS TOKEN SECRET"

"""Used to connect to the Twitter client
"""
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)
"""Check if the keys are correct.
"""
try:
    api.verify_credentials()
    print("Bot is online")
    connect = True
except:
    print("Bot has a problem")

keep_alive()
while connect:
	"""Check if it's time to post the tweet, especially here 6am"""
	
	actually_time = datetime.now()
	if actually_time.hour + 1 == 6 and actually_time.minute == 0:
		"""Start by recovering the sound of the day, then isolate the link and the cover of this music. Then create mp4 video which will contain audio and cover. Finally, post the tweet, and delete the files that are no longer needed."""
		try:

			musicOfDay = get_trackOfDay()

			link_video = musicOfDay[0].link
			link_cover = musicOfDay[0].album["cover_xl"]

			get_audio(link_video)		
			get_image(link_cover)

			files = False
			while files == False:
				try:
					with open('uploads/songOfDay.mp3'): pass
					with open('uploads/short_audio.mp3'): pass
					with open('uploads/coverOfDay.jpg'): pass
					files = True
				except:
					time.sleep(2)

			time.sleep(30)
			create_functional_video()

			tweet = upload(api, musicOfDay)

			if tweet == 1:
				print("Tweet posted")
				os.remove('uploads/video.mp4')
				os.remove('uploads/video.avi')
				os.remove('uploads/coverOfDay.jpg')
				os.remove('uploads/songOfDay.mp3')
				os.remove('uploads/short_audio.mp3')

		except Exception as Error:
			smtp_address = 'smtp.gmail.com'
			smtp_port    = "PORT (INT)"
			smtp_context = ssl.create_default_context()
			email        = "EMAIL"
			password     = "PASSWORD"

		with smtplib.SMTP_SSL(smtp_address, smtp_port, context=smtp_context) as server:
			server.login(email, password) 
			server.sendmail(email, "EMAIL THAT RECEIVES THE ERROR MAIL", str(Error))

	else:
		time.sleep(30)