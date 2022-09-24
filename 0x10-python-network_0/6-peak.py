#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ function that finds a peak in a list of unsorted integers """
    list_length = len(list_of_integers)
    if list_length == 0:
        return (None)
    peak = max(list_of_integers)
    if len(set(list_of_integers)) > 2:
        for i in range(list_length):
            if i != (list_length - 1):
                if ((list_of_integers[i] > list_of_integers[i + 1]) and
                   (list_of_integers[i] > list_of_integers[i - 1])):
                    peak = list_of_integers[i]
                    break
            else:
                peak = list_of_integers[(list_length - 1)]
    return (peak)
