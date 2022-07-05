#!/usr/bin/python3
"""JSON conversion to objects"""
import json


def load_from_json_file(filename):
    """A function that creates an object from a JSON file

    Args:
        filename : file to write into

    Returns:
        the object.

    """

    with open(filename) as f:
        return json.load(f)
