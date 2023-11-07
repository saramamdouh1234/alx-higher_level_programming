#!/usr/bin/python3
"""save_to_json_file module."""
import json


def load_from_json_file(filename):
    """Creates an Object ."""
    with open(filename, 'r') as f:
        return json.load(f)
