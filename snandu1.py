import nltk
from nltk import word_tokenize
import pandas as pd
import numpy as np
from datetime import datetime

tweets=list()
with open("dota.txt",encoding='utf8') as f:
    content = f.readlines()
for item in content:
    temp=list()
    tokens = word_tokenize(item)
    username = tokens[0]
    createdAt = datetime.strptime(tokens[2],"%d/%b/%Y:%H:%M:%S")
    text = ' '.join(tokens[5:len(tokens)-3])
    followers = int(tokens[len(tokens)-2])
    retweetCount = int(tokens[len(tokens)-1])
    temp.append(username)
    temp.append(createdAt)
    temp.append(text)
    temp.append(followers)
    temp.append(retweetCount)
    tweets.append(temp)

tweetsDataframe=pd.DataFrame(tweets, columns=['username', 'createdAt','text','followers','retweetCount'])
tweetsDataframe = tweetsDataframe.sort_values(by=['createdAt'],ascending=True)

#Top n users who have tweeted the most related to the search string for the entire timeline
TenMostTweetedUsers=tweetsDataframe['username'].groupby(tweetsDataframe['username']).count().reset_index(name="count").sort_values(by=['count'],ascending=False)[0:10]
TenMostTweetedUsers.to_csv('TenMostTweetedUsers.csv', sep='|')
print(TenMostTweetedUsers)

#Top n users who have tweeted the most for every hour
S = tweetsDataframe.createdAt
j=6
for i, hourlyDataframe in tweetsDataframe.groupby([(S - S[0]).astype('timedelta64[h]')]):
    time="Time: "+str(j)+" to "+str(j+1)
    print("\n"+time+"\n")
    if(j>22):
        j=0
    j=j+1
    df = hourlyDataframe['username'].groupby(hourlyDataframe['username']).count().reset_index(name="count").sort_values(by=['count'],ascending=False)[0:10]
    filename = "hour"+str(j)+".csv"
    df.to_csv(filename, sep='|')
    print (df)

#Top n users who have the maximum followers
TopTenUsersWithMostFollowers=tweetsDataframe.sort_values(by=['followers'],ascending=False).drop_duplicates(subset=['username'],keep='first')[:10]
TopTenUsersWithMostFollowers.to_csv('TopTenUsersWithMostFollowers.csv', sep='|')
print(TopTenUsersWithMostFollowers)

#Top n tweets which have the maximum retweet count
TopTenTweetsWithMostRetweets=tweetsDataframe.sort_values(by=['retweetCount'],ascending=False)[:10]
TopTenTweetsWithMostRetweets.to_csv('TopTenTweetsWithMostRetweets.csv', sep='|')
print(TopTenTweetsWithMostRetweets)