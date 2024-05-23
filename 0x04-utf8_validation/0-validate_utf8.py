#!/usr/bin/python3
"""UTF-8 data test function"""


def validUTF8(data):
    """Validates if data is utf-8 encoded"""
    if (not isinstance(data, list) or
       not all(map(lambda x: isinstance(x, int), data))):
        return False
    return all(map(lambda el: el < 128 and !(el & 0b10000000), data))
