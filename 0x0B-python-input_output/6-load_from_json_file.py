#!/usr/bin/python3
"""load text from json file"""
import json


def load_from_json_file(filename):
    """load object from json file"""

    with open(filename) as f:
        my_text = f.read()
        return json.loads(my_text)
