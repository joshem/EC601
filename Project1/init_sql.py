import mysql.connector

connect = mysql.connector.connect(user='josh',password='password',host='localhost')
mycur = connect.cursor(buffered=True)
mycur.execute("CREATE DATABASE MINIPROEJECT3")
