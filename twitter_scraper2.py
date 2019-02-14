#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy
import csv
import json
import pandas as pd


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

maximum_number_of_tweets_to_be_extracted = int(input('Enter the number of tweets that you want to extract- '))

# Mention the hashtag that you want to look out for

hashtag = input('Enter the hashtag you want to scrape- ')

i=0
 
#message,favorite_count,retweet_count,created_at,screen_name,user_mentions,retweeted_text,followers_count=[],[],[],[],[],[],[],[]

ids,retweet,favorite,inreplyto,friends,screen_name,followers,listed,text,location = [],[],[],[],[],[],[],[],[],[]
for tweet in tweepy.Cursor(api.search, q='#' + hashtag,rpp=100).items(maximum_number_of_tweets_to_be_extracted):
	ids.append(tweet.user.id)
	retweet.append(tweet.retweet_count)
	favorite.append(tweet.favorite_count)
	inreplyto.append(tweet.in_reply_to_screen_name)
	friends.append(tweet.user.friends_count)
	screen_name.append(tweet.user.screen_name)
	followers.append(tweet.user.followers_count)
	listed.append(tweet.user.listed_count)
	text.append(tweet.text)
	location.append(tweet.user.location)
	#print(tweet)
	# message.append(tweet.text)
	# favorite_count.append(tweet.favorite_count)
	# retweet_count.append(tweet.retweet_count)
	# #print(tweet.entities.user_mentions)
	# #user_mentions.append(tweet.user_mentions)
	# followers_count.append(tweet.user.followers_count)
	# created_at.append(tweet.created_at)
	# screen_name.append(tweet.user.screen_name)
	i=i+1
	if(i%100 == 0):
		print("Extracted " + str(i) +" tweets")
  

df=pd.DataFrame({'ids':ids, 'retweet': retweet, 'favorite': favorite, 'inreplyto':inreplyto,
	'friends':friends, 'screen_name':screen_name, 'followers':followers,
	'listed':listed, 'text':text, 'location':location})
            

# df=pd.DataFrame({'Message':message,
#                 'Favourite Count':favorite_count,
#                 'Retweet Count':retweet_count,
#                 'Created At':created_at,
#                 #'user_name':user_name,
#                 #'user_mentions':user_mentions,
#                 'followers_count':followers_count,
#                 'screen_name':screen_name})
# ,
#                 'user_mentions':user_mentions})

df.to_csv('tweets_with_hashtag_' + hashtag + '.csv')

print ('Extracted ' + str(maximum_number_of_tweets_to_be_extracted) + ' tweets with hashtag #' + hashtag)

#print(df)