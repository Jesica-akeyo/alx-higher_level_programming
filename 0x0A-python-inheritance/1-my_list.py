#!/usr/bin/python3
"""
This module contains class MyList
"""


class MyList(list):
    """ The class MyList inherits from list """
    def print_sorted(self):
        """ Method that prints the sorted list """
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
