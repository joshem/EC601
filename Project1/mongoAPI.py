import pymongo
import datetime
import operator

def new_session(username, numimg, desc):
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	db = myclient["miniproject3"]
	col = db["username"]
	now = datetime.datetime.now()
	str_now = str(now)
	entry = {"username":username, "daytime":str_now,"imgs": numimg, 'describers': desc }
	tmp = col.insert_one(entry)
	print(tmp.inserted_id)

def user_count():
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	db = myclient["miniproject3"]
	col = db["username"]
	cnt = {}
	for c in col.find():
		if(c['username'] in cnt):
			cnt[c['username']] = str(int(cnt[c['username']]) + int(c['imgs']))
		else:
			cnt[c['username']] = c['imgs']
	return cnt
	
def parser(desc):
	ret_desc = []
	tmp_word = ""
	for d in desc:
		if (d != ",") and (d !=" "):
			tmp_word = tmp_word + d
		else:
			if(tmp_word != ""):
				ret_desc.append(tmp_word)
			tmp_word=""
	ret_desc.append(tmp_word)
	return ret_desc

def popular():
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	db = myclient["miniproject3"]
	col = db["username"]
	desc = {}
	for i in col.find():
		tmp_desc = parser(i['describers'])
		for j in tmp_desc:
			if(j in desc):
				desc[j] = desc[j] +1
			else:
				desc[j] = 1
		sort_desc = sorted(desc.items(), key=operator.itemgetter(1))
		sort_desc.reverse()
		return sort_desc
		
def search(key):
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	db = myclient["miniproject3"]
	col = db["username"]
	keyUser = {}
	for col in col.find():
		if(key in col['describers']):
			if(col['username'] in keyUser):
				keyUser[col['username']].append(col['daytime'])
			else:
				keyUser[col['username']] = []
				keyUser[col['username']].append(col['daytime'])
	return keyUser
	

	
	

	
	
