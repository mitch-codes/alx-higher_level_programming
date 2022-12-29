#!/usr/bin/python3
# 100-safe_print_integer_err.py

import sys

def safe_print_integer_err(value):
    """
    A function that prints an integer
    """
    result = False
    try:
        print("{:d}".format(value))
        result = True
    except ValueError as e:
        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        return result
