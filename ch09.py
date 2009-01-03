#!/usr/bin/env python

# chapter 9 - XML Processing

from xml.dom import minidom
xmldoc = minidom.parse('data.xml')
print xmldoc
print xmldoc.toxml()

node = xmldoc.firstChild
print node.toxml()

nodelist = node.childNodes
print nodelist

print node.childNodes[1].toxml()
print node.childNodes[3].toxml()

#pg 187
s = u'Dive In'
print s

s = u'La Pe\xf1a'
print s

#pg 195
dataNodes = xmldoc.getElementsByTagName('data')
print dataNodes
for n in dataNodes:
  print n.toxml()
  for a in n.attributes.keys():
    print "%s='%s'" % (n.attributes[a].name, n.attributes[a].value)