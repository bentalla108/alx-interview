#!/usr/bin/python3
def canUnlockAll(boxes):
    if len(boxes) == 0:
        return False

    opened_boxes = set()

    opened_boxes.add(0)

    key_stack = boxes[0]

    while key_stack:
        key = key_stack.pop()

        if key < len(boxes) and key not in opened_boxes:
            opened_boxes.add(key)

            key_stack.extend(boxes[key])

    return len(opened_boxes) == len(boxes)
