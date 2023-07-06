#!/usr/bin/python3

"""Module solves lockboxes problem"""


def can_unlock_all(boxes):
    """
    Solves the lockboxes problem.

    Parameters:
    - boxes (list): A list of lists representing the boxes.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.

    Description:
    The can_unlock_all function determines if it is possible to
    unlock all the boxes based on the given list of boxes.
    A key with the same number as a box opens that box.

    """

    # Create a list to keep track of the opened status of each box
    opened = [False] * len(boxes)
    opened[0] = True

    stack = [0]

    while stack:
        box = stack.pop()

        for key in boxes[box]:

            if key < len(boxes) and not opened[key]:
                opened[key] = True
                stack.append(key)

    return all(opened)
