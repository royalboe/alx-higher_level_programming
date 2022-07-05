#!/usr/bin/python3
"""Appending to a text file"""


def append_write(filename="", text=""):
    """A functions that writes a string to a text file and returns the number
     of characters written

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.

    Returns:
        The number of characters appended.

    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
