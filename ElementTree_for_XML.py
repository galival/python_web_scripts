#connect to Etree to parse XML
import xml.etree.ElementTree as ET 

data = ET.parse(filename) #var filename
extract = data.findall(pattern) #var pattern

for entry in extract:
	#code
