#!/usr/bin/env python3


def canUnlockAll(boxes):
    if len(boxes) == 0 or len(boxes) == 1:
        return True
    keys = {}

    for key in range(len(boxes)):
        keys[str(key)] = False

    for i in range(len(boxes)):
        for key in boxes[i]:
            if key < len(boxes) and key != i:
                keys[str(key)] = True
    keys['0'] = True
    for key in keys:
        if not keys[key]:
            return False
    return True
