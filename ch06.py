#!/usr/bin/env python

# pg 98
try:
    fsock = open('/notafile','r')
except IOError:
    print "The file does not exist!"
print "processing done."

# pg 105
logfile = open('test.log','w')
logfile.write('test succeeded')
logfile.close()
print file('test.log').read()
logfile = open('test.log','a')
logfile.write('\nline 2')
logfile.close()
print file('test.log').read()

#pg 107
li = ['a', 'b', 'c']
for s in li:
    print s
    
print "\n".join(li)

for i in range(5):
    print i
    
li = ['a', 'b', 'c', 'd', 'e']
for i in range(len(li)):
    print li[i]

#pg 108
import os
for k, v in os.environ.items():
    print "%s=%s" % (k, v)
print

print "\n".join(["%s=%s" % (k, v) for k, v in os.environ.items()])

#pg 110
import sys
print "\n".join(sys.modules.keys())

print
#pg 114
print os.listdir("c:\\")
print
dirname = "c:\\"
print [f for f in os.listdir(dirname) if os.path.isfile(os.path.join(dirname,f))]
print
print [f for f in os.listdir(dirname) if os.path.isdir(os.path.join(dirname,f))]
