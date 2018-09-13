#!/usr/bin/env bash

#run twitter api program
myPicture = "twitterimage000.jpg"
if[ -f $(myPicture); then
	ffmpeg -f image2 -i image%d.jpg imagestovideo.mpg #edit this?
	#run Google API program
else
	echo "No picture found!"
fi
