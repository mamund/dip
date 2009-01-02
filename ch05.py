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

class counter2:
    __count = 0
    def __init__(self):
        pass #self.__count += 1
    def Increment(self):
        self.__count += 1
        return self.__count
        
print counter2
c = counter2()
print c.Increment()
d = counter2()
print d.Increment()
print c.Increment()
print c.Increment()
print c.Increment()
print d.Increment()

