#!/usr/bin/python3
"""using json to convert text object into json format"""
import json


def to_json_string(my_obj):
    """returns text or object in json format"""

    return json.dumps(my_obj)
