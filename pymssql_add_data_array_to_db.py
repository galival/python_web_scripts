# add an array of data into mssql database

#one arg is an int
category = 0

cursor.executemany(
	"INSERT INTO images VALUES (%s, %s, %s, %d)",
	#data array
	[('title1', 'description1','alt1', category),
	('title2', 'description2','alt2', category),
	('title3', '','', category)]
	)

conn.commit()