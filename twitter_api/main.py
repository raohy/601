import tweepy
consumer_key=''
consumer_secret=''
n=100
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
str1=api.search_tweets(q='lol world',count=n)
print(str1)
print(str1[0]._json['text'])
with open('data.txt', 'w',encoding="utf-8") as f:
    for i in range(n):
        f.write('}')
        for key in str1[i]._json:
            f.write('\n')
            f.writelines('"' + str(key) + '": ' + str((str1[i]._json[key])))
        f.write('\n'+'}')
