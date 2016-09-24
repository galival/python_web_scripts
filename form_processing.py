#python form processing script
import cgi

#place in script before #main program

def getData():
	data = cgi.FieldStorage()
	inputname = data.getvalue('inputname') #'inputname' is the name= attribute in the form
	return inputname

	#in the try block, call getData()

	inputname = getData()
	print ("Hello {0}".format(inputname))