import mysql.connector
import datetime
import operator
import os
import sys
import sqlAPI

user = input("Your username: ")
num  = input("Num o pics to downlaod: ")

os.system("./FinalSprint.sh" + num)

words = open("TwitImgs.txt").read().splitlines()
describers = ""
for word in words:
	describers = describers + word + ", "
d_len = len(describers)
describers = describers[0:d_len-2]
sqlAPI.new_session(user,num,describers)

cnt = sqlAPI.user_count()
print(cnt)


pop = sqlAPI.popular()
print(pop)

key = sqlAPI.search('fun')
print(key)

