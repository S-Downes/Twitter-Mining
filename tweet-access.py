import json
import tweepy
from tweepy import OAuthHandler
from twitter import get_auth, twitter_api

count = 10
query = 'Dublin'
api = twitter_api()

# Get all status
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

# Return results in json format
for result in results:
    print(json.dumps(result._json, indent=4))

# Return some attributes
for status in results:
    print(status.text.encode('utf-8'))
    print(status.user.id)
    print(status.user.screen_name)
    print(status.user.followers_count)
    print(status.place)
