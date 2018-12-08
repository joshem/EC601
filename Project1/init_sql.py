import mysql.connector
import sys
def make():
	connect = mysql.connector.connect(user='josh',password='password',host='localhost')
	mycur = connect.cursor(buffered=True)
	mycur.execute("CREATE DATABASE MINIPROEJECT3")
	
def clean():
	connect = mysql.connector.connect(user='josh',password='password',host='localhost',database='MINIPROEJECT3')
	mycur = connect.cursor(buffered=True)
	try:
		mycur.execute("DROP TABLE users")
	except:
		pass
		
if __name__=="__main__":
	argStr = str(sys.argv[1])
	if(argStr == "run"):
		make()
	elif(argStr == "clean"):
		clean()
	else:
		print("invalid input")

