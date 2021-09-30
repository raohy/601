import tweepy
import csv
consumer_key=''
consumer_secret=''
token=''
n=100
try:
    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    api = tweepy.API(auth)
except tweepy.TweepError:
    print('key in not verified')
str1=api.search_tweets(q='boston%20AND%20weather%20AND%20-%23boston%20-has%3Alinks%20-has%3Amedia%20-has%3Aimage%20-has%3Avideos',count=n,until='2021-09-23')
if not str :
    raise Exception('x is empty，api not respond')
with open('data.txt', 'w',encoding="utf-8") as f:
    for i in range(n):
        for key in str1[i]._json:
            if key=='text':
                f.write('\n')
                f.writelines('"' + str(key) + '": ' + str((str1[i]._json[key])))
store=[]
for i in range(n):
    for key in str1[i]._json:
        if key=='text':
            temp=[]
            temp.append(str((str1[i]._json[key])))
            store.append(temp)
with open('data_1.csv','w',encoding='UTF8',newline='') as f:
    writer = csv.writer(f)
    writer.writerows(store)
print(str1)
