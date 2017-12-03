"""Day 3: 'Spiral Memory' https://adventofcode.com/2017/day/3."""

from math import sqrt
import itertools
import numpy as np
import pytest


def day_3_part_1(target):
    # base case
    if target == 1:
        return 0

    # target ring level
    n = int(sqrt(target) - 1) // 2 + 1
    corner = (2*n + 1)**2

    # find closest corner
    while corner >= target:
        corner += -2*n
    # back off to 2nd to last corner in ring level
    corner += 2*n

    # compute L1 distance to origin
    width = 2*n + 1
    distance = max([ abs(target - corner), abs(target - corner) - width//2])

    # integer division doesn't necessarily simplify!
    L1_norm = 2 * (width//2) - distance

    return L1_norm


@pytest.mark.parametrize("inp,expected", [
    (1, 0),
    (12, 3),
    (23, 2),
    (1024, 31),
])
def test_day_3part_1_cases(inp, expected):
    computed = day_3_part_1(inp)
    assert computed == expected


# ------ Part 2

def day_3_part_2(target):
    n = 100
    A = np.zeros((n, n))

    def sum(A, a, b):
        result = 0
        for i, j in itertools.product([-1, 0, 1], [-1, 0, 1]):
            result += A[a + i, b + j]
        return result

    a, b = n//2, n//2
    A[a, b] = 1

    for k in range(1, 50):
        a, b = a, b + 1
        A[a, b] = sum(A, a, b)

        width = 2*k + 1
        for i in range(width - 2):
            a, b = a - 1, b
            A[a, b] = sum(A, a, b)
        for i in range(width - 1):
            a, b = a, b - 1
            A[a, b] = sum(A, a, b)
        for i in range(width - 1):
            a, b = a + 1, b
            A[a, b] = sum(A, a, b)
        for i in range(width - 1):
            a, b = a, b + 1
            A[a, b] = sum(A, a, b)

        if A.max() > target:
            A = np.sort(A.flatten())
            idx = np.searchsorted(A, target)
            return int(A[idx])


@pytest.mark.parametrize("inp,expected", [
    (130, 133),
    (200, 304),
])
def test_day_3part_2_cases(inp, expected):
    computed = day_3_part_2(inp)
    assert computed == expected


if __name__ == '__main__':
    # show solution
    main_inp = 265149
    print("Day 3.1 solution:", day_3_part_1(main_inp))
    print("Day 3.2 solution:", day_3_part_2(main_inp))

    # run verification tests
    pytest.main([__file__])
