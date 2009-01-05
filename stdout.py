#!/usr/bin/env python

#stdout.py

import sys

print 'Dive In'
saveout = sys.stdout
fsock = open('out.log','w')
sys.stdout = fsock
print 'This mesage will be logged instead of displayed'
sys.stdout = saveout
fsock.close()


