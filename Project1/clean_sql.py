import mysql.connector
import datetime
import operator

connect = mysql.connector.connect(user='josh',password='password',host='localhost',database='MINIPROEJECT3')
mycur = connect.cursor(buffered=True)
try:
	mycur.execute("DROP TABLE users")
except:
	pass