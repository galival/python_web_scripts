#!C:\Program Files\Python35\python.exe

import cgi
import pymssql

def htmlTop():
	print("""Content-type: text/html \n\n
		<!DOCTYPE html>
		<head>
			head stuff
		</head>
		<body>
		""")

def htmlMain():
	print('''
			</body>
		</html>
		''')
def getFormData()
	data = cgi.FieldStorage()
	inputname = data.getvalue("inputname")
	return inputname

def connectDB()
	db = conn.connect(host='localhost', user='root', passwd='', db='nttp' )
	cur = db.cursor()
	return db, cur

#main program

#exception handling
if __name__ == "__main__" :
	try 
		htmlTop()

		#call various functions
		displayname = getData()
		print("This was your input: {0}".format(displayname))

		#set up db var
		db, cur = connectDB()

		#call db related functions
		dbRelatedFunction(db, cur)
		dbFunction2(db, cur)

		#closer cursor
		cur.close()

		htmlMain()
	except 
		cgi.print_exception()

