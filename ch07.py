#!/usr/bin/env python

# chapter 7 - regular expressions
import re

#ppg 121-123
li = ['100 NORTH MAIN ROAD','100 NORTH BROAD ROAD','100 BROAD ROAD','100 BROAD ROAD APT. 3']
for s in li:
  print re.sub(r'\bROAD\b','RD.',s)

# ppg124-132
pattern = """
^                 # beginning of the string
M{0,4}            # thousands : 0 to 4 Ms
(CM|CD|D?C{0,3})  # hundreds : 900 (CM), 400 (CD), 0-300 (0-3-Cs), 5- 800 (D followed by 0-3 Cs)
(XC|XL|L?X{0,3})  # tens : 90 (XC), 40 (XL), 0-30 (0-3 Xs), 50-80 (L followed by 0-3 Xs)
(IX|IV|V?I{0,3})  # ones : 9 (IX), 4 (IV), 0-3 (0-3 Is), 5-8 (V followed by 0-3 Is)
$                 # end of string
"""

print 'M'
print re.search(pattern, 'M', re.VERBOSE)
print 'MCMLXXXIX'
print re.search(pattern, 'MCMLXXXIX', re.VERBOSE)
print 'MMMMDCCCLXXXVIII'
print re.search(pattern, 'MMMMDCCCLXXXVIII', re.VERBOSE)
print 'M'
print re.search(pattern, 'M')

#ppg 133-138
phonePattern = re.compile(r'''
            # don't match beginning of string
  (\d{3})   # area code
  \D*       # optional non-digit separator
  (\d{3})   # three digit trunk
  \D*       # optional sep
  (\d{4})   # station number
  \D*       # optional sep
  (\d*)     # optional extension
  $         # end of string
  ''', re.VERBOSE)

print phonePattern.search('work 1-(800) 444.1212 #1234').groups()
print phonePattern.search('800-555-1212').groups()
print phonePattern.search('work 1-(800) 444.1212 ext. 999').groups()

