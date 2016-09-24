#python looping structure for parsing dicts in XML format
#	start var False. checks for correct key, sets var to True, loops through next key which you know contains the desired value and since var is True, returns value.
#	That key is not "key", so var is again set to False
#	n = the dict passed
#	k = value of key tag code block passes

def lookup(n, k):
	found = False
	for child in n:
		if found return child.text
		if child.tag == "key" and child.text = k 
			found = True
	return None


#to parse whole XML file
filename = 
pattern = 'dict/dict/dict'


data = ET.parse(filename)
extract = data.findall(pattern)

for each in extract 
	if (lookup(each, 'primary_key_ID')) is None : continue #return to for loop

	#set each variable in relation you are trying to populate
	title = lookup(each, 'title')
	size = lookup(each, 'size')
	location = lookup(each, 'filepath')
	#above are examples of how to parse jpg data 
	#convert jpg to xml or parse jpg?

	if title is None or size is None or location is None : continue

	print title, size, location