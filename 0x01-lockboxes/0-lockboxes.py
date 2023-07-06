#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Function: can_unlock_all()

    Description:
    Determines if all the boxes can be unlocked based on the given list of boxes.
    A key with the same number as a box opens that box.

    Parameters:
    - boxes (list[list]): A list of lists representing the boxes and their corresponding keys.

    Return Type:
    bool: True if all boxes can be opened, False otherwise.

    Additional Considerations:
    - The first box (boxes[0]) is assumed to be unlocked.
    - The function checks for valid box structures and keys.

    """

    if not all(isinstance(box, list) for box in boxes):
        print('La boîte doit contenir que des boîtes')
        return False

    if (boxes[0] == [0] or boxes[0] == [] or
            not all(isinstance(cle, int) for cle in boxes[0])):
        print('La boîte [0] doit contenir une clé valide')
        return False

    # Create a list of box numbers starting from 1
    numero_box = list(range(1, len(boxes)))

    for box_index, box in enumerate(boxes):
        for key in box:
            if key != box_index and key in numero_box:
                numero_box.remove(key)

    return len(numero_box) == 0
