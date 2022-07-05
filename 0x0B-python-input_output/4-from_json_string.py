#!/usr/bin/python3
"""JSON conversion of objects"""
import json


def to_json_string(my_str):
    """A functions that returns the python representation of a string

    Args:
        my_str (:str:): string to be converted
.
    Returns:
        python representation of the object.

    """

    return json.loads(my_str)
