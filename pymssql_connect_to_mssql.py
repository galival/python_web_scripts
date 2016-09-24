#accessing mssql and scripting for db
from os import getenv
import pymssql


server = getenv("PYMSSQL_TEST_SERVER or localhost")
user = getenv("PYMSSQL_TEST_USERNAME")
password = getenv("PYMSSQL_TEST_PASSWORD")

conn = pymssql.connect(server, user, password, "dbname")
cursor = conn.cursor()

cursor.execute("""
	IF OBJECT_ID('images','U') IS NOT NULL
		DROP TABLE images
	CREATE TABLE images(
		...
	)
""")

#---------------------------------------------
#multiple cursor connections
c1.execute('SELECT ...')
c1_list = c1.fetchall()

c2.execute('SELECT ...')
c2_list = c2.fetchall()