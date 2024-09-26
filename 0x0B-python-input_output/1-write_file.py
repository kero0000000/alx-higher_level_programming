#!/usr/bin/python3
"""Difining write_file with two arguments"""
def write_file(filename="", text=""):
"""reads filename with UTF-8"""
with open (filename, "w" encoding='UTF-8') as f:
return f.write(text)
