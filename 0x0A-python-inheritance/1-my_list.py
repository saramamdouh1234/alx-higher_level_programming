#!/usr/bin/python3
"""MyList module"""


class MyList(list):
    """Inherits from list"""
    def print_sorted(self):
        """Print a sorted list"""
        print(sorted(self))
