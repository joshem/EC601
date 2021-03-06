import tweepy
#from tweepy import OAuthHandler
import sys
import wget
import json

import getPassword
myScreenname = 'JoshMan63909666' #screen name variable
twitCnt = 20
#put it all in try-except block for error handling
try:
	#OAuthHandler stuff
	auth = tweepy.OAuthHandler(getPassword.API_KEY, getPassword.API_SECRET_KEY)
	auth.set_access_token(getPassword.ACCESS_TOKEN, getPassword.ACCESS_TOKEN_SECRET)
except:
	print ("Can't connect to Twitter API. Consider checking your API keys?")
	sys.exit(0)
myAccnt = tweepy.API(auth)
#grab tweets from my account
myTweets = myAccnt.user_timeline(screen_name=myScreenname,count=twitCnt)
#extract the photos from these Tweets
myPics = []
try:
	for tweet in myTweets:
		media = tweet.entities.get('media',[])
		if(len(media)>0):
			myPics.append(media[0]['media_url'])
except:
	print("Error retrieving images from Twitter. Possible reasons: invalid Twitter account, internet connection, no images tied to account, etc.")
	sys.exit(0)
	#print(myPics)
	#using wget, download these pics into a folder, using a standardized naming system
	#standardized naming allows for predictable file names, makes iteration easier in later sections
cnt = 100
for pic in myPics:
	picPath = "./TwitterPics/TwitPic"
	cntStr = str(cnt)
	extension = ".jpg"
	newPicPath = picPath + cntStr + extension
	wget.download(pic,newPicPath)
	cnt = cnt + 1

		
	
