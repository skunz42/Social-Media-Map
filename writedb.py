import sqlite3
import csv

connection = sqlite3.connect("cities.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM city")

with open('metro-data.csv', mode='w', newline='') as metro_file:
    csv_writer = csv.writer(metro_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(384):
        result = cursor.fetchone()
        csv_writer.writerow(result)

connection.close()
