#!/usr/bin/env python

# chapter 8 - HTML Processing

# pg 151
import urllib
sock = urllib.urlopen("http://diveintopython.org")
htmlSource = sock.read()
sock.close()
print htmlSource

#pg 153
import urllib,urllister
usock = urllib.urlopen('http://diveintopython.org')
parser = urllister.URLLister()
parser.feed(usock.read())
usock.close()
parser.close()
for url in parser.urls:
  print url

#pg 159
def foo(arg):
  x = 1
  print locals()
print foo(7)
print foo('bar')

#pg 160
def foo(arg):
  x = 1
  print locals()
  locals()["x"] = 2
  print "x=",x
z = 7
print "z=",z
foo(3)
globals()["z"] = 8
print "z=",z

#pg 161
params = {"server":"mpilgrim", "database":"master", "uid":"sa","pwd":"secret"}
print "%(pwd)s" % params
print "%(pwd)s is not a good password for %(uid)s" % params
print "%(database)s of mind, %(database)s of body." % params