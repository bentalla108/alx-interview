#!/usr/bin/python3
""""
Calculates the fewest number of operations needed
to result in exactly 'n' H characters in the file.
"""


def minOperations(n):

    """
    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations required.

    If n is impossible to achieve, returns 0.

    Example:
        min_operations(9)  # Returns 6
    """
    if n < 1:
        return 0

    operations = 0
    paste_count = 1
    h_count = 1

    while h_count < n:
        if n % h_count == 0:
            operations += 2
            paste_count = h_count
            h_count *= 2
        else:
            operations += 1
            h_count += paste_count

    return operations
