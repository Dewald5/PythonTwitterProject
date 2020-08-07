# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 13:08:26 2020

@author: Dewald
"""


import tweepy
import matplotlib.pyplot as plt
import pandas as pd
from tweepy import OAuthHandler
 
consumer_key = 'chppDoy3i8wZTLCy7eZDkSopJ'
consumer_secret = 'ur0MVNOyvBKHponM0rhO6KNgRsith3LKeSOo0C5qD6anfa4NH6'
access_token = '1291306417287307264-pvZ3yK8ksdvW4j2kNMw6SAnu8YHZtP'
access_secret = 'YdEZ2111JFXJ0SgboeNVwjPOSrINYMc9ATo0ivaaAunPj'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

search_words = input("What do you want to be visualised in the graph\n")
#date_since = input("What date do you want it(YYYY-MM-DD)\n") sadly cant seen to get this function working properly
amount_tweets = int(input("How many tweets do you want visualised\n"))
tweets = tweepy.Cursor(api.search,
              q=search_words,
              lang="en",
              until="").items(amount_tweets) #since="date_since"

users_alldata = [[tweet.user.screen_name, tweet.user.location, tweet.user.created_at] for tweet in tweets]
tweet_text = pd.DataFrame(data = users_alldata, 
                    columns=['user', 'location','time'])

print(tweet_text)
tweet_text.plot()
plt.xlabel('Amount of tweets({})'.format(amount_tweets))
plt.ylabel('Date "{}" was tweeted'.format(search_words))
plt.title('Twitter Graph')