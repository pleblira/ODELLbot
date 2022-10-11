import tweepy
import os
from dotenv import load_dotenv, find_dotenv
import random
from apscheduler.schedulers.blocking import BlockingScheduler

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

main_message = "good morning, stay humble and stack sats"

alternate_message_list = ["good morning, we will win","good morning if you do not stand up for yourself nobody else will","good morning bitcoin represents hope to millions who need better money","good morning our house is on fire and corrupt politicians want to block the exit","good morning bitcoin represents hope to millions who need better money","good morning, if you do not stay humble bitcoin will humble you","good morning if you cannot spend your bitcoin without permission then it is not your bitcoin","good morning every time you use a credit card you are providing intimate financial and location data to your provider and their partners","good morning prepared bitcoiners are stronger than complacent cuckcoiners","good morning investment real estate is a shitcoin","good morning, stay humble, stack sats, and learn bitcoin privacy best practices","good morning, stay humble, stack sats, and learn how to use bitcoin"]


def tweepy_send_tweet_automated(tweet_message):
    draw_if_main_or_alternate_message = random.randint(1,4)
    print(draw_if_main_or_alternate_message)
    if draw_if_main_or_alternate_message == 1:
        tweet_message = alternate_message_list[random.randint(1,len(alternate_message_list)-1)]
    else:
        tweet_message = main_message
        
    consumer_key = os.environ.get("CONSUMER_KEY")
    consumer_secret = os.environ.get("CONSUMER_SECRET")
    access_token = os.environ.get("ACCESS_TOKEN")
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
    
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    print(tweet_message)
    api = tweepy.API(auth)
    api.update_status(tweet_message)


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tweepy_send_tweet_automated, 'cron', hour=9, minute=00, timezone="America/New_York")
    print('Press Ctrl+{0} to stop scheduler and switch to manual tweet.'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("\nScheduler stopped. Starting manual tweet functionality.\n\n")
        pass