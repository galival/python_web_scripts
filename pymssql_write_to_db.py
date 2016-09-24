# writing to db

def insertTable(db, cur, data)
	for each in data
		sql = "INSERT INTO table values ({0}, {1}, {2})".format(each[0], each[1], each[2]) #any parameters
		cursor.execute(sql)
	db.commit()