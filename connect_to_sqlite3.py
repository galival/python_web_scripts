#set up sqlite3

import sqlite3

conn = sqlite3.connect('dbname')
cur = conn.cursor()

cur.execute('''SQL code

	''')
cur.executescript('''
	multiple SQL scripts
	''')

cur.commit()

cur.close()