#!/usr/bin/env python3
"""UTF-8 data test function"""


def validUTF8(data):
    """Validates if data is utf-8 encoded"""
    return all(map(lambda el: el | 0b11111111 == 255, data))
