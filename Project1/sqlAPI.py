import mysql.connector
import operator
import datetime

def new_session(user, imgnum, des):
	connect = mysql.connector.connect(user='josh',password='password',host='localhost',database='MINIPROEJECT3')
	mycur = connect.cursor(buffered=True)
	try:
		mycur.execute("CREATE TABLE users (username VARCHAR(255), daytime VARCHAR(255), imgs VARCHAR(255), describers VARCHAR(1000))")
	except:
		pass
	now = datetime.datetime.now()
	now_str = str(now)
	mycur.execute("""INSERT INTO users (username, daytime, imgs, describers) VALUES (%s, %s, %s, %s)""", (user, now_str, imgnum, des))
	connect.commit()

def user_count():
	connect = mysql.connector.connect(user='josh',password='password',host='localhost',database='MINIPROEJECT3')
	mycur = connect.cursor(buffered=True)
	try:
		mycur.execute("CREATE TABLE users (username VARCHAR(255), daytime VARCHAR(255), imgs VARCHAR(255), describers VARCHAR(1000))")
	except:
		pass
	cmd = "SELECT * FROM users"
	mycur.execute(cmd)
	imgcnt = mycur.fetchall()
	userCnt = {}
	for c in imgcnt:
		if(c[0] in userCnt):
			userCnt[c[0]] = str(int(userCnt[c[0]]) + int(c[2]))
		else:
			userCnt[c[0]] = c[2]
	return userCnt

def parser(des):
	newD = []
	tmpS = ""
	for d in des:
		if(d != ",") and (d != " "):
			tmpS = tmpS + d
		else:
			if(tmpS != ""):
				newD.append(tmpS)
			tmpS = "" #reinit
	newD.append(tmpS) #last bit
	return newD

def popular():
	connect = mysql.connector.connect(user='josh',password='password',host='localhost',database='MINIPROEJECT3')
	mycur = connect.cursor(buffered=True)
	try:
		mycur.execute("CREATE TABLE users (username VARCHAR(255), daytime VARCHAR(255), imgs VARCHAR(255), describers VARCHAR(1000))")
	except:
		pass
	cmd = "SELECT * FROM users"
	mycur.execute(cmd)
	pop = mycur.fetchall()
	desc = {}
	for p in pop:
		tmp_d = parser(p[3])
		for tmp in tmp_d:
			if(tmp in desc):
				desc[tmp] = desc[tmp] + 1
			else:
				desc[tmp] = 1
	sortedDes = sorted(desc.items(),key=operator.itemgetter(1))
	sortedDes.reverse()
	return sortedDes

def search(key):
	connect = mysql.connector.connect(user='josh',password='password',host='localhost',database='MINIPROEJECT3')
	mycur = connect.cursor(buffered=True)
	try:
		mycur.execute("CREATE TABLE users (username VARCHAR(255), daytime VARCHAR(255), imgs VARCHAR(255), describers VARCHAR(1000))")
	except:
		pass
	cmd = "SELECT * FROM users"
	mycur.execute(cmd)
	res = mycur.fetchall()
	keyUser = {}
	for r in res:
		if(key in r[3]):
			if(key[0] in keyUser):
				keyUser[r[0]].append(r[1])
			else:
				keyUser[r[0]]=[]
				keyUser[r[0]].append(r[1])
	return keyUser
