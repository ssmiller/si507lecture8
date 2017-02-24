import sqlite3

conn = sqlite3.connect('music.db')
cur = conn.cursor()

statement = 'CREATE TABLE IF NOT EXISTS '
statement += 'Tracks (title TEXT, artist TEXT, album TEXT, plays INTEGER)'
cur.execute(statement)

statement = 'INSERT INTO Tracks VALUES (?, ?, ?, ?)'
data = ('London Calling', 'The Clash', 'London Calling', 235)
cur.execute(statement, data)
conn.commit()

statement = 'DELETE FROM Tracks'
cur.execute(statement)
conn.commit()

conn.close()