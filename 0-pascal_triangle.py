#usr/bin/env python3
"""module for implementing the pascal triangle"""


def pascal_triangle(n):
    """Draws the Pascal triangle"""
    if n <= 0:
        return []

    pascal = []
    if n >= 1:
        pascal.append([1])
        if n == 1:
            return pascal
    if n >= 2:
        pascal.append([1, 1])
        if n == 2:
            return pascal
    
    while (n - 2):
        row = [1]
        for x, y in zip(pascal[-1][0:len(pascal)], pascal[-1][1:]):
            row.append(x + y)
        row.append(1)

        pascal.append(row)

    return pascal
