#!/usr/bin/env python

# pg 75
import types
print types.FunctionType
# print FunctionType # error w/o types qualifier
from types import FunctionType
print FunctionType

# pg 76
class Loaf:
    pass # pass is no-op, works as empty braces for C#

# pg 80
import fileinfo
f = fileinfo.FileInfo("test")
print f.__class__
print f.__doc__
print f

# pg 93
class counter:
    count = 0
    def __init__(self):
        self.__class__.count += 1

print counter
print counter.count
c = counter()
print c.count
print counter.count
d = counter()
print d.count
print c.count
print counter.count
