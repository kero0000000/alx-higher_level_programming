#!/usr/bin/python3
"""Difining append_write function"""
def append_write(filename="", Text=""):
"""appends filename With UTF-8"""
with open(filename, 'a' , encoding="UTF-8") as f:
     return f.write(text)
