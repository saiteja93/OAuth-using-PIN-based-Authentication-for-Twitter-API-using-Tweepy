#!/usr/bin/python 2.7
# -*- coding: utf-8 -*-
#Author : Saiteja Sirikonda



import tweepy
import json
import time

consumer_key="ENTER APPROPRIATE CUSTOMER KEY"
consumer_secret= "ENTER APPROPRIATE CUSTOMER SECRET KEY"

def GetUserAccessKeySecret():
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

	# get access token from the user and redirect to auth URL
	authen_url = auth.get_authorization_url()
	print 'Authorization URL: ' + authen_url

	# ask user to verify the PIN generated in broswer
	verify = raw_input('PIN: ').strip()

	try:
	    auth.get_access_token(verify)
	except tweepy.TweepError:
	    print 'Error! Failed to get access token.'
	    time.sleep(60*15)

	ACCESS_KEY = auth.access_token
	ACCESS_SECRET = auth.access_token_secret
		#print 'ACCESS_KEY = {}'.format(auth.access_token)
	#print 'ACCESS_SECRET = {}'.format(auth.access_token_secret)

	# authenticate and retrieve user name
	auth.set_access_token(auth.access_token, auth.access_token_secret)
	api = tweepy.API(auth)	
	return ACCESS_SECRET

GetUserAccessKeySecret()

def GetProfile(username):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

	# get access token from the user and redirect to auth URL
	authen_url = auth.get_authorization_url()
	print 'Authorization URL: ' + authen_url

	# ask user to verify the PIN generated in broswer
	verify = raw_input('PIN: ').strip()

	try:
	    auth.get_access_token(verify)
	except tweepy.TweepError:
	    print 'Error! Failed to get access token.'
	    time.sleep(60*15)

	ACCESS_KEY = auth.access_token
	ACCESS_SECRET = auth.access_token_secret
		#print 'ACCESS_KEY = {}'.format(auth.access_token)
	#print 'ACCESS_SECRET = {}'.format(auth.access_token_secret)

	# authenticate and retrieve user name
	auth.set_access_token(auth.access_token, auth.access_token_secret)
	api = tweepy.API(auth)
	status = api.user_timeline(user=username, count=1)[0]		
	json_str = json.dumps(status._json)

	return json_str

GetProfile("ANY USERNAME")