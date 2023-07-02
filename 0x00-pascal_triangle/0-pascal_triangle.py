#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the given number of rows.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list: Pascal's triangle represented as a list of lists.

    Raises:
        TypeError: If the input n is not an integer.
        ValueError: If the input n is less than or equal to 0.
    """

    if isinstance(n, int):
        if n <= 0:
            return []

        pascal = [[0] * (i+1) for i in range(n)]

        for i in range(n):
            pascal[i][0] = 1
            for j in range(1, i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
            pascal[i][i] = 1

        return pascal
