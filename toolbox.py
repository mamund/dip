#!/usr/bin/env python

# toolbox
def openAnything(source):
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
