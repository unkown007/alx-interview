#!/usr/bin/python3
"""Defines N queens puzzle challenge of placing N non-attacking queens on an
NxN chessboard
"""


def queens(n, i, a, b, c):
    """Find all N non-attacking quuens on an NxN chessboard"""
    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                yield from queens(n, i+1, a+[j], b+[i+j], c+[i-j])
    else:
        yield a


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    for solution in queens(n, 0, [], [], []):
        new_solution = [[i, x] for i, x in enumerate(solution)]
        print(new_solution)
