#!/usr/bin/python3
def canUnlockAll(boxes):
    if not all(isinstance(box, list) for box in boxes):
        print('La boîte doit contenir que des boîtes')
        return False

    if (
        boxes[0] == [0]
        or boxes[0] == []
        or not all(isinstance(cle, int) for cle in boxes[0])
    ):
        print('La boîte [0] doit contenir une clé valide')
        return False

    numero_box = list(range(len(boxes)))

    for i, box in enumerate(boxes):
        for key in box:
            if key != i and key in numero_box:
                numero_box.remove(key)
                print(key)

    return len(numero_box) == 0
