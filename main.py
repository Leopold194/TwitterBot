import tweepy as tw

from deezpy.search import Search

consumer_key = "CE8nS8CNhhXGWm7GUQHQIc3yU"
consumer_secret = "zB8RP1eZnCysTTFGmYFGluXtpe7lwZ3OvaABWSAK63QsWYk6ex"

access_token = "1265572530640879616-h8IELazz0SPIWr121kyWvlHdkPiBY5"
access_token_secret = "7Rfc26cVIbqN5UjD4gq5lHDdDTTCStCdfSy9cilTPXgT4"

#client = tw.Client(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token = access_token, access_token_secret = access_token_secret)
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)