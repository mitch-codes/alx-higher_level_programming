#!/usr/bin/python3
"""using json to convert text object into json format and write it into a file"""
import json


def save_to_json_file(my_obj, filename):
    """write json into a file"""

    with open(filename, mode='w') as f:
        f.write(json.dumps(my_obj))
