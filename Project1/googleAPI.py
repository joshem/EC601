import io
import os
from google.cloud import vision
from google.cloud.vision import types
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/josh/Desktop/googleCreds.json" #change this to your path
client= vision.ImageAnnotatorClient()
print ("outside loop");
picCnt=100
extension=".jpg"

while(picCnt<10000):
	try:
		filePathPrefix="./TwitterPics/TwitPic"
		picCntStr = str(picCnt)
		picCnt= picCnt + 1
		filePath = filePathPrefix + picCntStr + extension
		if(os.path.exists(filePath)!=True):
			break
		#print(filePath)
		with io.open(filePath,'rb') as picFile:
			content = picFile.read()
		image = types.Image(content=content)
		#print("after file")
		response = client.label_detection(image=image)
		labels = response.label_annotations

		picNum = picCnt - 7000
		print("description of picture with path",filePath,"is: ")
		for label in labels:
			print(label.description)
	except:
		print("Something went wrong")
		break
