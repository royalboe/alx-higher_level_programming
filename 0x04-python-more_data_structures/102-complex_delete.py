#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for k, v in a_dictionary:
        if v == value:
            del a_dictionary[k]
    return a_dictionary
