import sqlite3
import praw

connection = sqlite3.connect("cities.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM city")
result = cursor.fetchall()

for r in result:
    print(r)

connection.close()
