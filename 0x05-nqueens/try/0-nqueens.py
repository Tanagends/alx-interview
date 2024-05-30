#!/usr/bin/python3
"""N-queens backtracking algorithm"""
import sys

sol = []

def main():
    """N-queens backtracking algorithm"""
    n = validate()
    
    backtrack(n, [])


def backtrack(n, lst):
    """backtracks"""
    if n = 0:
        sol.append(lst)

    else:
        for _ in range

def validate():
    """Validates user's input
       Raises an error and exits if input is invalid
       Else: Returns a valid n
    """
    args = sys.argv
    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(args[1])
    except ValueError, TypeError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    return n


if __name__ == '__main__':
    main()
