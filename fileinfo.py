#!/usr/bin/env python

class FileInfo(dict):
    "store file metadata"
    def __init__(self, filename=None):
        self["name"] = filename
        