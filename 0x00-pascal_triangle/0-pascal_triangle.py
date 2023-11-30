#!/usr/bin/python3
"""Define pascal_triangle function"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal's triangle of n
    Args:
        n(int): integer number
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(0, n):
        j = 0
        elem = []
        while j <= i:
            if j == 0 or j == i:
                elem.append(1)
            elif (j > 0 and i > 1) and j < i:
                elem.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            j += 1
        triangle.append(elem)
    return triangle
