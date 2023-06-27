import mysql.connector

databse = mysql.connector.connect(
    root = 'localhost',
    user = 'root',
    passwd = '0000'
)

#prepare cursor object
cursorObject = databse.cursor()

# Create a Database

cursorObject.execute("CREATE DATABASE customer")

print("Database Created")