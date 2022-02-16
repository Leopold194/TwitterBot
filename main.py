import tweepy as tw

from deezpy.search import Search

consumer_key = "Y0w1V5Fx08E9YVwb8yeEQZkTJ"
consumer_secret = "tbXHOsf1DFyhxzr2YePJzIz3BXWkIJ2GHk0Zx8YsRnNkfnyhGq"

access_token = "1494014284761907203-fDqNtiqF7sJ8S5Xy5hdcnxSXcMVUl0"
access_token_secret = "nhcarTONHrDHEWvgbyw1G7uhSq2feubhICba4M3eDrRBT"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)

try:
    api.verify_credentials()
    print("Bot is online")
except:
    print("Bot has a problem")

api.update_status("test")