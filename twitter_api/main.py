import tweepy
consumer_key=''
consumer_secret=''
n=100
try:
    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    api = tweepy.API(auth)
except tweepy.TweepError:
    print('key in not verified')
str1=api.search_tweets(q='lol world',count=n)
if !str :
    raise Exception('x is empty，api not respond')
with open('data.txt', 'w',encoding="utf-8") as f:
    for i in range(n):
        f.write('}')
        for key in str1[i]._json:
            f.write('\n')
            f.writelines('"' + str(key) + '": ' + str((str1[i]._json[key])))
        f.write('\n'+'}')
