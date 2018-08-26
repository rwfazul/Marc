import sys
import tweepy

import pymongo
from pymongo import MongoClient

from authenticate import api_tokens

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        # Identifica se não é um retweet
        if(not status.retweeted and 'RT @' not in status.text[0:4] and status.lang == "pt"):
            tweet = status._json

            tweet['text'] = tweet['text'].replace('\n', ' ').replace('\r', '')

            if("atrasa" in tweet['text']):
                tweet['prob_type'] = "atrasado"

            elif("extravi" in tweet['text'] or "perdid" in tweet['text']):
                tweet['prob_type'] = "extraviado"

            elif("danificad" in tweet['text'] or "quebrad" in tweet['text']):
                tweet['prob_type'] = "danificado"

            else:
                tweet['prob_type'] = "none"

            tweets = db.tweets
            tweets.insert_one(tweet).inserted_id

            print("-----------------------------------------")
            print("Lang:", tweet['lang'])
            print("Text:", tweet['text'])
            print("Prob:", tweet['prob_type'])

        return True; # Don't kill the stream

    def on_error(self, status_code):
        print('Encountered error with status code:', status_code)
        print("-----------------------------------------")

        return True # Don't kill the stream

    def on_exception(self, exception):
        print('Exception: ', exception)
        print("-----------------------------------------")

        return True # Don't kill the stream

    def on_timeout(self, timeout):
        print('Timeout: ', timeout)
        print("-----------------------------------------")

        return True # Don't kill the stream

# Start the Stream Listener
def start_stream():
    print ("---------- STREAMING STARTED -----------")

    while True:
        try:
            myStream = tweepy.streaming.Stream(auth, MyStreamListener())

            myStream.filter(track=["atraso", "atrasado","atrasada", "extravio", "extraviado", "extraviada", "perdido", "danificado", "quebrado"], stall_warnings=True)

        except ValueError:
            print('ERROR: Exeption occurred!' + ValueError)
            print("-----------------------------------------")

            continue

if __name__ == '__main__':
    # Variables that contains the user credentials to access Twitter API
    key = api_tokens()

    # Tweepy API authentication
    auth = tweepy.OAuthHandler(key['consumer_key'], key['consumer_secret'])
    auth.set_access_token(key['access_token'], key['access_token_secret'])

    # API authentication
    api = tweepy.API(auth)

    client = MongoClient('localhost', 27017)
    db = client['hackaton']

    start_stream()