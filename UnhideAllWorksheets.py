from xml.dom import minidom
import os
import lxml.etree as et

## Rename the file

#os.rename('testdata.twb',"testdata.xml")

   
xmldoc = et.parse('test3.xml')

root = xmldoc.getroot()

for window in root.iter('window'):
	if window.get('class') == ('hidden-worksheet'):
		window.set('class', 'worksheet')
		#print window.get('class')

xmldoc.write('output.xml', encoding = 'utf-8', pretty_print=True,inclusive_ns_prefixes='xsi')
os.rename('output.xml',"output.twb")

#itemlist = xmldoc.element();

#print itemlist;


#xmldoc.write('test2.xml')


# # ## parse the XML doc

# xmldoc = minidom.parse('testdata.xml')

# ##find the window of the sheet

# itemlist = xmldoc.getElementsByTagName('window') [4]


# #itemlist.pop(0)
 
#  ## set the class to worksheet and test

# print itemlist.getAttribute('class')

# itemlist.setAttribute('class' , 'worksheet')

# print itemlist.getAttribute('class')

# #os.rename('testdata.xml',"testdata.twb")


# xmldoc = et.parse('testdata.xml')

# xmldoc.write('test2.xml')


# #print itemlist[0].attributes['name'].value

# # for s in itemlist[1:] :
# #      print s.attributes['name'].value

