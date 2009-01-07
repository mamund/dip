#!/usr/bin/env python

#ch11.py

import httplib

#pg 230
httplib.HTTPConnection.debuglevel = 1
import urllib
feeddata = urllib.urlopen('http://amundsen.com/blog/feed/').read()

# pg 231
# note changed code here to fix bug in book
print
import urllib2
h=urllib2.HTTPHandler(debuglevel=1)
request = urllib2.Request('http://amundsen.com/blog/feed/')
request.add_header('User-Agent','mca-agent/1.0')
opener = urllib2.build_opener(h)
feeddata = opener.open(request).read()

#232
print
import urllib2
h=urllib2.HTTPHandler(debuglevel=1)
request = urllib2.Request('http://amundsen.com/blog/feed/')
opener = urllib2.build_opener(h)
ds1 = opener.open(request)
print ds1.headers.dict
request.add_header('if-modified-since',ds1.headers.get('last-modified'))
try:
  ds2 = opener.open(request)
except:
  print 'error!'

#235
print
import urllib2
h=urllib2.HTTPHandler(debuglevel=1)
request = urllib2.Request('http://amundsen.com/blog/feed/')
opener = urllib2.build_opener(h)
ds3 = opener.open(request)
print ds3.headers.dict
request.add_header('if-match',ds3.headers.get('etag'))
try:
  ds4 = opener.open(request)
except:
  print 'error!'

#pg 236
"""
print
print 'pg 236'
import urllib2,httplib
h=urllib2.HTTPHandler(debuglevel=1)
request = urllib2.Request('http://demo-pa.mymediabox.com/admin/')
opener = urllib2.build_opener(h)
f = opener.open(request)
print f.url
print f.headers.dict
print f.status
"""

#pg 241
print
print 'pg 241'
import urllib2,httplib
h=urllib2.HTTPHandler(debuglevel=1)
request = urllib2.Request('http://amundsen.com/examples/sds-photos/')
request.add_header('accept-encoding','gzip')
request.add_header('Connection','Keep-Alive')
opener = urllib2.build_opener(h)
f = opener.open(request)

#pg242
cdata = f.read()
print len(cdata)
import StringIO
cstream = StringIO.StringIO(cdata)
import gzip
gzipper = gzip.GzipFile(fileobj=cstream)
data = gzipper.read()
print data
print len(data)


