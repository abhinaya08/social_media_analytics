#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy
import csv
import json

#!/usr/bin/python
# -*- coding: utf-8 -*-

# create a dictionary to store your twitter credentials

twitter_cred = dict()

# Enter your own consumer_key, consumer_secret, access_key and access_secret
# Replacing the stars ("********")

twitter_cred['CONSUMER_KEY'] = 'Pxuj5YQCvLkkhEOujd59G9x28'
twitter_cred['CONSUMER_SECRET'] = 'ch0Gy1Y8RRzBwQf4rGu76hPy6P78B71CCBZWTIZ4JRDF5W4LTZ'
twitter_cred['ACCESS_KEY'] = '262621283-fSIt1baOf7CVhgHk9qTVwzJtbdT2WwH6Ks8z6GNc'
twitter_cred['ACCESS_SECRET'] = 'tVr5iSndzO5yjZlsYoKCXMJDgjgi3iLgK7W5TjaFk59Yo'

# Save the information to a json so that it can be reused in code without exposing
# the secret info to public

with open('twitter_credentials.json', 'w') as secret_info:
json.dump(twitter_cred, secret_info, indent=4, sort_keys=True)

# Twitter API credentials

with open('twitter_credentials.json') as cred_data:
info = json.load(cred_data)
consumer_key = info['CONSUMER_KEY']
consumer_secret = info['CONSUMER_SECRET']
access_key = info['ACCESS_KEY']
access_secret = info['ACCESS_SECRET']

# Create the api endpoint

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

# Mention the maximum number of tweets that you want to be extracted.

maximum_number_of_tweets_to_be_extracted = \
int(input('Enter the number of tweets that you want to extract- '))

# Mention the hashtag that you want to look out for

hashtag = input('Enter the hashtag you want to scrape- ')

for tweet in tweepy.Cursor(api.search, q='#' + hashtag,
rpp=100).items(maximum_number_of_tweets_to_be_extracted):
with open('tweets_with_hashtag_' + hashtag + '.txt', 'a') as \
the_file:
the_file.write(str(tweet.text.encode('utf-8')) + '\n')

print ('Extracted ' + str(maximum_number_of_tweets_to_be_extracted) \
+ ' tweets with hashtag #' + hashtag)