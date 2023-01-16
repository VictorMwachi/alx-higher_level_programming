#!/bin/python3
"""
finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """returns largest integer fro the a list"""
    if len(list_of_integers) == 0:
        return None
    else:
        return max(list_of_integers)
