#!/usr/bin/env python

# chapter 10 - SCripts and Streams

# pg 198
import urllib
from xml.dom import minidom

usock = urllib.urlopen('http://amundsen.com/blog/feed/')
xmldoc = minidom.parse(usock)
usock.close()
print xmldoc.toxml()

#pg 199
contents = "<grammar><ref id='bit'><p>0</p><p>1</p></ref></grammar>"
xmldoc = minidom.parseString(contents)
print xmldoc.toxml()

#pg 200
import StringIO
ssock = StringIO.StringIO(contents)
print ssock.read()
print ssock.read()
ssock.seek(0)
print ssock.read(15)
print ssock.read()
ssock.close()

#pg 201
ssock = StringIO.StringIO(contents)
xmldoc = minidom.parse(ssock)
ssock.close()
print xmldoc.toxml()

#pg 202
print "-- openAnything --"
import toolbox

sock = toolbox.openAnything("http://amundsen.com/blog/feed/")
xmldoc = minidom.parse(sock)
sock.close()
print xmldoc.toxml()

#pg 203
for i in range(3):
  print 'Dive In'

import sys
for i in range(3):
  sys.stdout.write('Dive In\n')

for i in range(3):
  sys.stderr.write('Dive In\n')
