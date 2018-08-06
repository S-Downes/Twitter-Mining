import json
import tweepy
from tweepy import OAuthHandler
from twitter import get_auth, twitter_api

# Set YAHOO WOE ID's to preferred location
DUB_WOE_ID = 560743
OSLO_WOE_ID = 862592
TOKYO_WOE_ID = 1118370
KYOTO_WOE_ID = 15015372

# Return the trends for these locations
api = twitter_api()
dub_trends = api.trends_place(DUB_WOE_ID)
oslo_trends = api.trends_place(OSLO_WOE_ID)
tokyo_trends = api.trends_place(TOKYO_WOE_ID)
kyoto_trends = api.trends_place(KYOTO_WOE_ID)

#  Find common trends and differences for each of the cities
dub_trends_set = set([trend['name'] for trend in dub_trends[0]['trends']])
oslo_trends_set = set([trend['name'] for trend in oslo_trends[0]['trends']])
tokyo_trends_set = set([trend['name'] for trend in tokyo_trends[0]['trends']])
kyoto_trends_set = set([trend['name'] for trend in kyoto_trends[0]['trends']])

common_trends_db_os = set.intersection(dub_trends_set, oslo_trends_set)
common_trends_tk_ky = set.intersection(tokyo_trends_set, kyoto_trends_set)

difference_db_os = set.difference(dub_trends_set, oslo_trends_set)
difference_tk_ky = set.difference(tokyo_trends_set, kyoto_trends_set)

print("""COMMON TRENDS IN DUBLIN AND OSLO""")
print(common_trends_db_os)
print("""COMMON TRENDS IN TOKYO AND KYOTO""")
print(common_trends_tk_ky)

print("""DIFFERENT TRENDS IN DUBLIN AND OSLO""")
print(difference_db_os)
print("""DIFFERENT TRENDS IN TOKYO AND KYOTO""")
print(difference_tk_ky)
