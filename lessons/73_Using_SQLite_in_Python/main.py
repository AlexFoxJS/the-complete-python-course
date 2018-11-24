import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute('YOUR SQL QUERY HERE')
connection.commit()

connection.close()
