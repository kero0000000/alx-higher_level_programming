#!/usr/bin/python3
"""contains the "class_to_json" function"""
def class_to_json(obj):
"""returns the dictionary description with semple data structure
   (list, dictionary, string, integer and boolean)
   for json serialization of an object"""
   return obj.__dict__
