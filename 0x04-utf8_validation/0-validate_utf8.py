#!/usr/bin/python3
"""UTF-8 data test function"""


def validUTF8(data):
    """validates utf-8"""
    count = 0
    for num in data:
        num &= 0b11111111
        if count == 0:
            if num >> 5 == 110:
                count = 2
            elif num >> 4 == 1110:
                count = 3
            elif num >> 3 == 11110:
                count = 4
            elif count >> 7:
                return False
        else:
            if num >> 6 != 0b10:
                return False
            count -= 1
    return count == 0
