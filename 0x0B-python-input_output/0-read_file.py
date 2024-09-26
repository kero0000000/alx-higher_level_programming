#!/usr/bin/python3
"""Difining read_file function"""
def read_file(filename=""):
"""reads filename with UTF-8"""
with open (filename, encoding= 'UTF-8') as f:
print(f.read(), end="")
