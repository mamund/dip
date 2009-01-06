#!/usr/bin/env python

#sampleargs.py

import sys
import getopt

def main(argv):
  try:
    opts,args = getopt.getopt(argv,"hg:d", ["help", "grammar=", "debug"])
  except getopt.GetoptError:
    print 'argument error!'
    sys.exit(2)

if __name__ == "__main__":
  main(sys.argv[1:])
