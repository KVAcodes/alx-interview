#!/usr/bin/python3
""" contains the lockbox problem solution.
"""


def canUnlockAll(boxes):
    for idx_1 in range(1, len(boxes)):
        flag = False
        for idx_2 in range(len(boxes)):
            if idx_1 == idx_2:
                continue
            if idx_1 in boxes[idx_2]:
                flag = True
        if flag is not True:
            return False
    return True
