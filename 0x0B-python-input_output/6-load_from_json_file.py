#!/usr/bin/python3
"""
This module creates an Obj from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    Function that creates an obj from a JSON file
    filename: file name
    """
    with open(filename, 'r') as f:
        data = f.read()
        return json.loads(f)
