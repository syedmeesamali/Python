import os
import zipfile

#regular expression matching
import re

#to pretty print the XML content
import xml.dom.minidom

document = zipfile.ZipFile('../docs/CV - Presca.docx')
print(document.namelist())

uglyXml = xml.dom.minidom.parseString(document.read('word/fontTable.xml')).toprettyxml(indent='  ')
text_re = re.compile('>\n\s+([^<>\s].*?)\n\s+</', re.DOTALL)    
prettyXml = text_re.sub('>\g<1></', uglyXml)

#print(prettyXml)

#Turn xml content into a string
xml_content = document.read('word/document.xml')
document.close()

xml_str = str(xml_content)

link_list = re.findall('http.*?\<', xml_str)[1:]
link_list = [x[:-1] for x in link_list]

print(link_list)
