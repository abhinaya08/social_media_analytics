import json

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