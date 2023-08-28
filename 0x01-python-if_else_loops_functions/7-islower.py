#!/usr/bin/python3
def islower(c):
    """
    Function that checks for lowercase character.
    """
    if ord(c) in range(97, 123):
        return True
    else:
        return False
