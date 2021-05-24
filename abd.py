import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="394Favorite"
)

print(mydb)
