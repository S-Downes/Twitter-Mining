import tweepy
from tweepy import OAuthHandler
from prettytable import PrettyTable
from twitter import get_auth, twitter_api

api = twitter_api()

user = api.get_user("@DigitalDeepBlg")

def get_user_data(user):
    print("Username: {0}".format(user.screen_name))
    print("User followers: {0}".format(user.followers_count))
    print("User statuses: {0}".format(user.statuses_count))
    print("User favourites: {0}".format(user.favourites_count))

get_user_data(user)

# Now print the same information for the user friends
for friend in user.friends():
    get_user_data(friend)

# Return most recent tweets from users this user follows
for status in tweepy.Cursor(api.home_timeline).items(10):
    print(status.text)
 