#!/usr/bin/python3
"""
A program that prints all possible different combinations of two digits.

Numbers are separated by ",", followed by a space
The two digits are different
01 and 10 are considered the same combination of the two digits 0 and 1
Print only the smallest combination of two digits
Numbers should be printed in ascending order, with two digits
The last number should be followed by a new line
You can only use no more than 3 print functions with string format
You can only use no more than 2 loops in your code
You are not allowed to store numbers or strings in a variable
You are not allowed to import any module
Running should give this output:
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23,
24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56,
57, 58, 59, 67, 68, 69, 78, 79, 89
"""
for i in range(0, 9):
    for j in range(i + 1, 10):
        if i < 8:
            print("{:d}{:d}".format(i, j), end=", ")
        else:
            print("{:d}{:d}".format(i, j))
