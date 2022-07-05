#!/usr/bin/python3
"""JSON conversion of objects"""
import json


def to_json_string(my_obj):
    """A functions that returns the JSON representation of an object

    Args:
        my_obj (:obj:): object to be converted
.
    Returns:
        JSOM format of the object.

    """

    return json.dumps(my_obj)
