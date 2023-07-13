#!/usr/bin/python3


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations
     needed to result in exactly 'n' H characters.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations required.

    Raises:
        TypeError: If 'n' is not an integer.

    Example:
        minOperations(9)  # Returns 6
    """
    if not isinstance(n, int) or n < 1:
        return 0
    op = n
    ctn = 0
    rest = 0

    while op != 1:
        rest = op % 2
        op = op // 2
        ctn = ctn + 2

    return ctn + rest
