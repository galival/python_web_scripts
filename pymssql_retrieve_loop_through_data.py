#retrieve and loop through data. tailored to newtothepublic.
#------------------------------------------

#get data from db

cursor.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')

row = cursor.fetchone()

while row:
    print("ID=%d, Name=%s" % (row[0], row[1]))
    row = cursor.fetchone()


def callGallery(gal)
	sql = 'SELECT * FROM images JOIN galleries ON images.gallery_ID = galleries.gallery_ID WHERE galleries.gallery_ID = (SELECT gallery_ID FROM galleries WHERE gallery = %s)', gal
	#alternate formatting:
	#sql = 'SELECT * FROM images JOIN galleries ON images.gallery_ID = galleries.gallery_ID WHERE galleries.gallery_ID = (SELECT gallery_ID FROM galleries WHERE gallery = {0})'.format(gal)
	c
	ursor.execute(sql)
	
	data = cusor.fetchall()
	
	return data

images = cursor.callGallery('prints')

for each in images
	#display
	print ("<div>...</div>")


conn.close()

#-------------------------------------------
#additional examples:

# displaying data from db
def getData()
	sql = "SELECT .."
	cur.execute()
	#fetch all results as list
	data = cur.fetchall()
	return data

def displayData(data)
	print("<html> template?")
	for each in data 
		print ("<div class='someclass'>{0}</div>".format(each[0]))

#-------------------------------------------
#additional parameters

cursor.fetchmany(size=n) #can use instead of including TOP n or LIMIT n in SQL

#execute many if you only have a few values that can be hardcoded or a few parameters to pass
cursor.executemany(sql, par1, par2, par3) #performs execution for each paramter



