#!/usr/bin/env python

#ch11.py

import httplib

httplib.HTTPConnection.debuglevel = 1
import urllib
feeddata = urllib.urlopen('http://amundsen.com/blog/feed/').read()

print
httplib.HTTPConnection.debuglevel = 1
import urllib2
request = urllib2.Request('http://amundsen.com/blog/feed/')
request.add_header('User-Agent','mca-agent/1.0')
print request.get_full_url()
opener = urllib2.build_opener()
feeddata = opener.open(request).read()
print 'all done'