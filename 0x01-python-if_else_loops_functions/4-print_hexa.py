#!/usr/bin/python3
"""
A program that prints the numbers from 0 to 98 in decimal
and in hexadecimal.
Do not import any module
"""
for i in range(0, 99):
    print("{:d} = 0x{:x}".format(i, i))
