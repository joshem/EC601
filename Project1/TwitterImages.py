import tweepy
from tweepy import OAuthHandler
import sys
import wget
import json

import getPassword

try:
	auth = tweepy.OAuthHandler(getPassword.API_KEY, getPassword.API_SECRET_KEY)
	auth.set_access_token(getPassword.ACCESS_TOKEN, getPassword.ACCESS_TOKEN_SECRET)
	myAccnt = tweepy.API(auth)

	myTweets = myAccnt.user_timeline(screen_name='JoshMan63909666',count=10)
	#myTweets = []
	#for tweet in tweepy.Cursor(myAccnt.user_timeline).items(10)
	#	myTweets.append(tweet)	
	myPics = []
	for tweet in myTweets:
		media = tweet.entities.get('media',[])
		if(len(media)>0):
			myPics.append(media[0]['media_url'])
	print(myPics)
	cnt = 0000

	for pic in myPics:
		picPath = "/home/josh/Desktop/EC601/Project1/TwitterPics"
		cntStr = str(cnt)
		extension = ".jpg"
		newPicPath = picPath + cntStr + extension
		wget.download(pic,newPicPath)
		cnt = cnt + 1
except:
	print("Wasn't unable to get pictures from Twitter.  Possibe considerations: Twitter is down, incorrect access key, or something else.")
	
