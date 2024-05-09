#!/usr/bin/python3
"""Minimum Operations function"""


def minOperations(n):
    """Calculates the fewest number of
    operations needed to result in exactly n H
    characters in this file.
    """
    pasted_chars = 1
    clipboard = 0
    counter = 0

    while pasted_chars < n:
        # If no characters are copied yet
        if clipboard == 0:
            # Copy all characters (this is equivalent to your "copyall" operation)
            clipboard = pasted_chars
            # Increment operations counter
            counter += 1

        # If only one character is pasted initially
        if pasted_chars == 1:
            # Paste characters from clipboard
            pasted_chars += clipboard
            # Increment operations counter
            counter += 1
            # Continue to the next iteration of the loop
            continue

        remaining = n - pasted_chars  # Calculate remaining characters to paste

        # Check if it's impossible to achieve n characters
        # because the clipboard has more characters than needed
        if remaining < clipboard:
            return 0

        # If remaining characters cannot be evenly divided by the current characters
        if remaining % pasted_chars != 0:
            # Paste the characters from the clipboard
            pasted_chars += clipboard
            # Increment operations counter
            counter += 1
        else:
            # Copy all characters again (this is equivalent to your "copyall" operation)
            clipboard = pasted_chars
            # Paste the characters from the clipboard
            pasted_chars += clipboard
            # Increment operations counter
            counter += 2

    # If the desired number of characters is achieved
    if pasted_chars == n:
        return counter
    else:
        return 0

