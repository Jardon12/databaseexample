import sqlite3

db = sqlite3.connect("chinook.db")
cur = db.cursor()
cur.execute("SELECT Name FROM artists")
result = cur.fetchall()
for artist in result:
    print(artist[0])

