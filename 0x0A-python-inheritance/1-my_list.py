#!/usr/bin/python3
"""class MyList that inherits from list"""

class MyList(list):

    def __init__(self):
        super().__init__()
    def print_sorted(self):
        """"prints  prints the list, but sorted (ascending sort)"""
        return sorted(self.list)
