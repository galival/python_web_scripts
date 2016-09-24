#retrieve data as dictionaries to access data by name/key rather than index
conn = pymssql.connect(server, user, password, "nttp")
cursor = conn.cursor(as_dict=True)
#saves data as {(id:1, name:al, city:baltimore), (id:2, name:bre, city:car)}
for row in data
	print ("%d, %s, %s") % (row['id'],row['name'],row['city']))