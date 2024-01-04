#!/usr/bin/python3
""" UTF-8 validator module
"""


def validUTF8(data):
    """ Validates data set with contains all UTF-8 codes pointes
    """
    nBytes = 0

    for x in data:
        mask = 1 << 7

        if nBytes == 0:
            while mask & x:
                nBytes += 1
                mask = mask >> 1

            if nBytes == 0:
                continue

            if nBytes == 1 or nBytes > 4:
                return False
        else:
            if not (x & (1 << 7) and not (x & (1 << 6))):
                return False

        nBytes -= 1

    if nBytes == 0:
        return True

    return False
