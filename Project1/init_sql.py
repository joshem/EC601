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
	action = input("Would you like to create or clean the databse? \nEnter 'Clean' to clean or 'Create' to create: ")
	action = str(action)
	#argStr = str(sys.argv[1])
	if(action == "Create"):
		make()
	elif(action == "Clean"):
		clean()
	else:
		print("invalid input")

