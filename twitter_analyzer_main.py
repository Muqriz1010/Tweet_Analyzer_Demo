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
import nltk
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt

keyword = "covid"
num_tweets = 100

stop_words = stopwords.words('english')
added_sw = ['dont','get','youre','aint','thats','would','know','cant'
           ,'shes','hes','im','like','rt']

def get_tweets(query, count):
    #get tweets from twitter
   api = tweepy.API(twa.auth,wait_on_rate_limit=True)
   search_tweet = tweepy.Cursor(api.search, query, lang="en").items(count)
   
   text_arr = []
   for tweet in search_tweet:
       text_arr.append(tweet.text)
   
  
   return text_arr
    
def add_stop_words(arr):
    #add stop words that was initialized above
	for e in arr:
		stop_words.append(e)

def clean_and_tokenize(arr):
    #clean up tweets by lowering caps, tokenize sentences into words, and remove stop words
   remove_caps = [word.lower() for word in arr]
   separator = ', '
   join_tweets = separator.join(remove_caps)
   removeurl = " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", join_tweets).split())
   text = nltk.word_tokenize(removeurl)
   #removing stop words
   tweet_nsw = [word for word in text if not word in stop_words]
   tweet_nsw_nc = [word for word in tweet_nsw if not word in keyword]
  
   return tweet_nsw_nc

def count_and_plot(arr):
    #count most common words mentioned in tweets
   word_count = Counter(arr).most_common(20)
   print(word_count)
   word_count = pd.DataFrame(word_count, columns=['words', 'count'])
   word_count.head()
   fig, ax = plt.subplots(figsize=(8, 8))

   # Plot horizontal bar graph
   word_count.sort_values(by='count').plot.barh(x='words',
                           y='count', ax=ax, color="purple")
   ax.set_title("Common Words Found in tweet search :" + keyword)
   plt.show()
  
   print(word_count)


if __name__ == "__main__":
    add_stop_words(added_sw)
    tweets = get_tweets(keyword, num_tweets)
    processed_tweets = clean_and_tokenize(tweets)
    count_and_plot(processed_tweets)






