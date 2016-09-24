#choose codes for project

#cycle through list of codes and enter 0 or 1 to choose
project_name = raw_input('project: ',)

codes_chosen = []

cursor.callproc(GetCodes) #select all codes

print('select 0 for no, 1 for yes')

option = cursor.fetchone()

while option:
	choice = raw_input()
	if (choice == 1) : codes_chosen.append(option)
	option = cursor.fetchone()


for code in codes_chosen : updateProjectCodes(project_name, codes_chosen)

	cursor.execute('''
		INSERT INTO dbo.project_codes (project_ID, code_ID)
		WHERE project_ID = (SELECT project_ID FROM project WHERE name = %s)
		AND code_ID = (SELECT code_ID FROM code WHERE code = %s)
		''', project, code)

def updateProjectCodes(project, codes) #string, string array
	for code in codes 
		#the above sql

	conn.commit()
	return None

#run sql query to check if it worked
for each in codes_chosen
	cursor.excute('''
		SELECT p.project_name AS 'project', c.code_name AS 'code' FROM projects AS p JOIN code AS c JOIN project_codes AS pc
		ON p.project_ID = pc.project_ID AND c.code_ID = pc.code_ID
		WHERE p.project_name = %s AND c.code_name = %s
		''', project_name, each)
	row = cursor.fetchone()
	print ('{0}\t, {1}\n'.format(row[0],row[1]))
