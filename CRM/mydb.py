import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = '0000'

	)
#prepare cursor object
cursorObject = dataBase.cursor()

# Create a Database

cursorObject.execute("CREATE DATABASE customer")

print("Database Created")