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

data_items = [
	('London Calling', 'The Clash', 'London Calling', 235),
	('Anarchy in the UK', 'The Sex Pistols', 'Nevermind the Bollocks', 144),
	('Blitzkrieg Bop', 'The Ramones', 'The Ramones', 89)
]

statement = 'INSERT INTO Tracks VALUES (?, ?, ?, ?)'

for item in data_items:
	cur.execute(statement, item)
conn.commit()

#Research impact of this method on potential SQL injection attacks

conn.close()