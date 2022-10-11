import tweepy
import os
from dotenv import load_dotenv, find_dotenv

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)


tweet_message = "good morning, stay humble and stack sats"


def tweepy_send_tweet(tweet_message,tweet_image):
    consumer_key = os.environ.get("CONSUMER_KEY")
    consumer_secret = os.environ.get("CONSUMER_SECRET")
    access_token = os.environ.get("ACCESS_TOKEN")
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
    
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)

    api = tweepy.API(auth)
    api.update_status(tweet_message)




if __name__ == '__main__':
    tweepy_send_tweet(tweet_message)

