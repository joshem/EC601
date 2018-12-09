import os
import sys
import mongoAPI

user = input("Your username: ")
num  = input("Num o pics to downlaod: ")

comand = "./FinalScript.sh"
os.system(comand)

words = open("TwitImgs.txt").read().splitlines()
describers = ""
for word in words:
	describers = describers + word + ", "
describers = describers[0:len(describers)-2]

mongoAPI.new_session(str(user),str(num),describers)


cnt = mongoAPI.user_count()
print(cnt)

pop = mongoAPI.popular()
print(pop)

key = mongoAPI.search('fun')
print(key)
