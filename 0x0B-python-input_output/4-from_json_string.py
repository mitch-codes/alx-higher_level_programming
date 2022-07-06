#!/usr/bin/python3
"""convert text in json to normal string format"""
import json


def from_json_string(my_str):
    """returns object in normal format"""

    return json.loads(my_str)
