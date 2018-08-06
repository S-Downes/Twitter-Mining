import json
import tweepy
from tweepy import OAuthHandler
from twitter import get_auth, twitter_api

# Set YAHOO WOE ID's to preferred location
DUB_WOE_ID = 560743
LON_WOE_ID = 44418

# Return the trends for these locations
api = twitter_api()
dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)

#  Find common trends for both cities using the set.intersection method
dub_trends_set = set([trend['name'] for trend in dub_trends[0]['trends']])

lon_trends_set = set([trend['name'] for trend in lon_trends[0]['trends']])

common_trends = set.intersection(dub_trends_set, lon_trends_set)

print(common_trends)
