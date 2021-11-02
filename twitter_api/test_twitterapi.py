import tweepy
import pytest
consumer_key=''
consumer_secret=''
token=''
n=100

def test_connection():
    assert connection() is not None

def connection():
    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    api = tweepy.API(auth)
    return api

def test_retrieve():
    assert retrieve() is None

def retrieve():
    api=connection()
    str1=api.search_tweets(q='boston%20AND%20weather%20AND%20-%23boston%20-has%3Alinks%20-has%3Amedia%20-has%3Aimage%20-has%3Avideos',count=n,until='2021-09-23')


