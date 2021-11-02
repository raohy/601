import tweepy
import csv
import pytest
consumer_key='nZVTNs0wavMUCiU5L9nklXVUK'
consumer_secret='YmfaDemXJkaZN4J8J7ZnwrGVp7ztGSImjd0ANr4BsiKgm6DqM0'
token='AAAAAAAAAAAAAAAAAAAAAOFLUAEAAAAAzDSj%2BmMe%2BuZlpX9q%2BKCSs5XDFDk%3Dl3ImkdzJ2iL9HlJNctvjP2g4VK1r8pfZZBDRXHAkhaW7Aey6xX'
n=100
# cli=tweepy.Client(bearer_token=token)
# cli.search_all_tweets(query='boston%20AND%20weather%20AND%20-%23boston%20-has%3Alinks%20-has%3Amedia%20-has%3Aimage%20-has%3Avideos')
# def test_connection():
#     with pytest.raises(tweepy.errors.TweepyException ):
#         connection()
#
# def connection():
#     try:
#         auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
#         api = tweepy.API(auth)
#         return api
#     except tweepy.TweepyException:
#         print('key in not verified')
def test_connection():
    assert connection() is not None

def connection():
    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    api = tweepy.API(auth)
    return api

def test_empty():
    assert retrieve() is None

def retrieve():
    api=connection()
    str1=api.search_tweets(q='boston%20AND%20weather%20AND%20-%23boston%20-has%3Alinks%20-has%3Amedia%20-has%3Aimage%20-has%3Avideos',count=n,until='2021-09-23')

# with open('data.txt', 'w',encoding="utf-8") as f:
#     for i in range(n):
#         for key in str1[i]._json:
#             if key=='text':
#                 f.write('\n')
#                 f.writelines('"' + str(key) + '": ' + str((str1[i]._json[key])))
# store=[]
# for i in range(n):
#     for key in str1[i]._json:
#         if key=='text':
#             temp=[]
#             temp.append(str((str1[i]._json[key])))
#             store.append(temp)
# with open('data14.csv','w',encoding='UTF8',newline='') as f:
#     writer = csv.writer(f)
#     writer.writerows(store)
# print(str1)
