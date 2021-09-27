import tweepy
consumer_key='nZVTNs0wavMUCiU5L9nklXVUK'
consumer_secret='YmfaDemXJkaZN4J8J7ZnwrGVp7ztGSImjd0ANr4BsiKgm6DqM0'
token='AAAAAAAAAAAAAAAAAAAAAOFLUAEAAAAAzDSj%2BmMe%2BuZlpX9q%2BKCSs5XDFDk%3Dl3ImkdzJ2iL9HlJNctvjP2g4VK1r8pfZZBDRXHAkhaW7Aey6xX'
n=100
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
str1=api.search_tweets(q='lol',count=n)
print(str1)
print(str1[0]._json['text'])
with open('data.txt', 'w',encoding="utf-8") as f:
    for i in range(n):
        f.write('}')
        for key in str1[i]._json:
            f.write('\n')
            f.writelines('"' + str(key) + '": ' + str((str1[i]._json[key])))
        f.write('\n'+'}')
