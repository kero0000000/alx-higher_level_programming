#!/usr/bin/python3
"""square medule."""
class square:
"""Defines a square."""
def __int__(self, size=0):
"""constructor.
Args:
size:length of a side of the square.
Raises:
typeerror:if size is not an integer
valeerror:if size is less than 0
"""
if not isinstance(size, int):
raise TypeError('size must be an integer')
if size < 0:
raise ValueError('size must be >= 0')
self.__size = size
