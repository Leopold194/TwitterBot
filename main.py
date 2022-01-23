import tweepy as tw

from deezpy.search import Search

auth = tw.OAuthHandler("zMnm4cb1pqpDkvHiuR23OtnIc", "dBfiSHyU3hGC4aHQSlpUCvMrCnlEBJJiV942D0YiMSJhybJWW1")
auth.set_access_token("1265572530640879616-fdWmNdQ1FyiTlThfJTXsRXRm80QLCA", "ykRX16GXGsEvUHXSlF5HKnHSOxH3Gli7l2KTOflAwar8n")

api = tw.API(auth)

try:
    api.verify_credentials()
    print("Connected Bot")
except:
    print("Launch Error")