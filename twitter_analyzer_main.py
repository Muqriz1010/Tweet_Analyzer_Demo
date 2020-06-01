#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 18:07:00 2020

@author: muqrizdevice
"""
import re
import tweepy
import twitter_analyzer_auth as twa
import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt

keyword = "umno"

api = tweepy.API(twa.auth,wait_on_rate_limit=True)

public_tweets = api.home_timeline()
#for tweet in public_tweets:
    #print(tweet.text)

search_tweet = api.search(q=keyword)

stop_words = stopwords.words('english')
added_sw = ['dont','get','youre','aint','thats','would','know','cant'
            ,'shes','hes','im','like','rt']

def add_stop_words(arr):
	for e in arr:
		stop_words.append(e)

add_stop_words(added_sw)


def filter_tweet(keyword):
    search_tweet = tweepy.Cursor(api.search, q=keyword, lang="en").items(100)
    #df = pd.DataFrame(t.__dict__ for t in search_tweet)
    #arr = df.to_numpy()
    #tweet_column = arr[:, [30]]
    text_arr = []
    for tweet in search_tweet:
        text_arr.append(tweet.text)
    #text_arr = df.to_numpy()
    
    return text_arr
    
    #return tweet_column
    #print(tweet_column)


def search_tweet(keyword):
    tweet_list = []
    for tweet in tweepy.Cursor(api.search, q=keyword).items(50):
        tweet_list.append(tweet.text)
    
    return tweet_list


def clean_tweets(arr):
    remove_caps = [word.lower() for word in arr] 
    separator = ', '
    join_test = separator.join(remove_caps)
    removeurl = " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", join_test).split())
    text = nltk.word_tokenize(removeurl)
    tweet_nsw = [word for word in text if not word in stop_words]
    tweet_nsw_nc = [word for word in tweet_nsw if not word in keyword]
    
    
    return tweet_nsw_nc


def count_and_plot(arr):
    nsw_counts = Counter(arr).most_common(20)
    print(nsw_counts)
    tweet_nsw_nc = pd.DataFrame(nsw_counts, columns=['words', 'count'])
    tweet_nsw_nc.head()
    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot horizontal bar graph
    tweet_nsw_nc.sort_values(by='count').plot.barh(x='words',
                            y='count', ax=ax, color="purple")
    ax.set_title("Common Words Found in tweet search :" + keyword)
    plt.show()
    
    print(tweet_nsw_nc)


tweet_arr = filter_tweet(keyword)
#print(tweet_arr)
dem_tweets = clean_tweets(tweet_arr)
count_and_plot(dem_tweets)


