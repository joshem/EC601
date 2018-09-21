#!/usr/bin/env bash

#run twitter api program
./clean.sh
python3 TwitterImages.py
cd TwitterPics/
pwd
myPicture = "TwitPic100.jpg"
#if file doesn't exist
if [ -f ${myPicture} ]; then
	#ffmpeg -framerate 1/5 -start_number 1000 -i twitterimage%04d.jpg -c:v libx264 -r 30 -pix_fmt yuv420p out.mp4
	#ffmpeg -framerate 1/5 -start_number 7000 -i TwitPic%d.jpg      -c:v libx264 -r 30 -pix_fmt yuv420p vid.mp4
	#ffmpeg -r 30 -f image2 -s 1920x1080 -start_number 7000 -i TwitPic%03d.jpg -vcodec libx264  -pix_fmt yuv420p test.mp4
	ffmpeg -f image2 -framerate 0.5 -y -i TwitPic1%02d.jpg -c:v libx264 -pix_fmt yuv420p out.mp4
	cd ..
	python3 googleAPI.py
	#run Google API program
else
	echo "No picture found!"
fi
