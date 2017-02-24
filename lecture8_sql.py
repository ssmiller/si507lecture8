'''
Created 2017-02-24 based on code provided by Professor Mark Newman in SI507 lecture.
'''

import sqlite3

# attach to the database file
conn = sqlite3.connect('music.db')
cur = conn.cursor()

# Create database and first table, unless they exist already
statement = 'CREATE TABLE IF NOT EXISTS '
statement += 'Tracks (title TEXT, artist TEXT, album TEXT, plays INTEGER)'
cur.execute(statement)

# insert one item into the table
statement = 'INSERT INTO Tracks VALUES (?, ?, ?, ?)'
data = ('London Calling', 'The Clash', 'London Calling', 235)
cur.execute(statement, data)
conn.commit()

# Clear the table to prevent duplicate items from being created
statement = 'DELETE FROM Tracks'
cur.execute(statement)
conn.commit()

# Add several entries to the table at once
data_items = [
	('London Calling', 'The Clash', 'London Calling', 235),
	('Anarchy in the UK', 'The Sex Pistols', 'Nevermind the Bollocks', 144),
	('Blitzkrieg Bop', 'The Ramones', 'The Ramones', 89)
]

statement = 'INSERT INTO Tracks VALUES (?, ?, ?, ?)'

for item in data_items:
	cur.execute(statement, item)
conn.commit()

# Research impact of this method on potential SQL injection attacks

def runquery(q):
	cur.execute(q)
	for row in cur:
		print(row)
	print('-' * 20)

# Example query
query = 'SELECT * FROM Tracks'
runquery(query)

query = 'SELECT title, plays FROM Tracks'
runquery(query)

query = 'SELECT title, plays FROM Tracks ORDER BY title'
runquery(query)

query = 'SELECT * FROM Tracks WHERE plays > 100'
runquery(query)

query = 'SELECT plays FROM Tracks WHERE artist = "The Ramones"'
runquery(query)




# close the database file to prevent locks
conn.close()