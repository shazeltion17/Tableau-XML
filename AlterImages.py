from xml.dom import minidom
import os
#import xml.etree.cElementTree as et
import tkFileDialog
import lxml.etree as tt
from bs4 import BeautifulSoup
import StringIO
## Rename the file
   
## Grab the Particular file to convert xml

#newfile = tkFileDialog.askopenfilename()
parser1 = tt.XMLParser(encoding='utf-8')

xmldoc = tt.parse('Proactive SAM Portfolio v1.47.xml', parser1 )

root  = xmldoc.getroot()

################################################################################################

##loop through to convert the images to the correct Path

##finds the intro dashboard and converts the image

for dashboard in root.iter('dashboard'):
	if dashboard.get('name') == "Intro":

		##Loops through the zones within a specified dashboard
		for zone in list(dashboard.iter('zone')):
			if zone.get('id') == ('88'):
				zone.set('param', 'customerFiles/Image/Intro - Top.png')		
	else:
		continue

##	Finds all other Dashboard images and converts them
for zone in root.iter('zone'):
	if zone.get('id') == ('12'):
		zone.set('param', 'customerFiles/Image/Logo - EMC.png')
		#print zone.get('param')

# Replace all values in the database section with DatabaseName

for column in root.iter('column'):
	if column.get('caption') =='Database Name' and column.get('datatype') == 'string' and column.get('name') =='[Parameter 11]':
		#print column.get('value')
		column.set('value', '"DatabaseName"')
		for calculation in list(column.iter('calculation')):
			#print calculation.get('formula')
			calculation.set('formula', '"DatabaseName"')

#Replace all values in the Host report Generated column with 127.0.0.1

for column in root.iter('column'):
	if column.get('caption') =='Host Report Generated' and column.get('datatype') == 'string' and column.get('name') =='[Parameter 12]':
		#print column.get('value')
		column.set('value', '"127.0.0.1"')
		for calculation in list(column.iter('calculation')):
			#print calculation.get('formula')
			calculation.set('formula', '"127.0.0.1"')

# Replace all values in the Date of workbook Generation column with 2012-12-12-12:12:12.12

for column in root.iter('column'):
	if column.get('caption') =='Date of Workbook Generation' and column.get('datatype') == 'datetime' and column.get('name') =='[Parameter 4]':
		#print column.get('value')
		column.set('value', '#2012-12-12-12:12:12.12#')
		for calculation in list(column.iter('calculation')):
			#print calculation.get('formula')
			calculation.set('formula', '#2012-12-12-12:12:12.12#')	


for datasource in root.iter('datasource'):
	if  datasource.get('inline') == 'true' and datasource.get('caption') == 'ecps_ehs_glossary (ecps_engr_ecps.ecps_ehs_glossary) (cps_dev01)':
		for connection in list(datasource.iter('connection')):
			if connection.get('class') == 'dataengine':
				connection.set('dbname' ,'customerFiles/Data/glossary/glossary.tde')
				#print connection.get('dbname')
				break
	elif  datasource.get('inline') == 'true' and datasource.get('caption') == 'SAM Proactive Portfolio':
		for connection in list(datasource.iter('connection')):
			if connection.get('class') == 'dataengine':
				connection.set('dbname' ,'customerFiles/Data/customer/customer.tde')
				#print connection.get('dbname')
				break


# ##################################################################################################		


xmldoc.write('output.xml', encoding = 'utf-8', pretty_print=True,inclusive_ns_prefixes='xsi')
os.rename('output.xml',"output.twb")