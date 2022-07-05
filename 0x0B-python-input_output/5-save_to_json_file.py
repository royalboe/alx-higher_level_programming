#!/usr/bin/python3
"""JSON conversion to objects"""
import json


def save_to_json_file(my_obj, filename):
    """A function that writes an object to a text file using a JSON format

    Args:
        my_obj (:obj:): object to be converted
        filename : file to write into
    Returns:
        the object.

    """

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
