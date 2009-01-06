#!/usr/bin/env python

#stderr.py

import sys

fsock = open('error.log','w',)
sys.stderr = fsock
raise Exception, 'this error will be logged'
