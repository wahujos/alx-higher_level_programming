#!/usr/bin/python3
"""Technical interview algorithm"""
# finds a peak in a list of unsorted integers
def find_peak(list_of_integers):
    """Find peak function algorith"""
    high = len(list_of_integers) - 1
    low = 0
    if not list_of_integers:
        return None
    while low < high:
        middle = (high + low) // 2
        if list_of_integers[middle] < list_of_integers[middle + 1]:
            low = middle + 1
        else:
            high = middle
    return list_of_integers[low]
