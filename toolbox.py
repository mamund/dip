#!/usr/bin/env python

# toolbox
def openAnything(source):
  if source == '-':
    import sys
    return sys.stdin

  # try to open with urllib
  import urllib
  try:
    return urllib.urlopen(source)
  except (IOError, OSError):
    pass

  # try to open as local file
  try:
    return open(source)
  except (IOError, OSError):
    pass

  # try to load as string
  import StringIO
  return StringIO.StringIO(str(source))