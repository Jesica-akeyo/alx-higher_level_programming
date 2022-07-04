#!/usr/bin/python3
"""
This module contains class MyList
"""


class MyList(list):
    def print_sorted(self):
        """ Method that prints the sorted list """
        print(sorted(self))
