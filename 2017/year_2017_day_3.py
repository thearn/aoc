"""Day 3: 'Spiral Memory' https://adventofcode.com/2017/day/3."""

from math import sqrt
import itertools
import numpy as np
import pytest


# ------------- Part 1


def day_3_2017_part_1(target):
    # base case
    if target == 1:
        return 0

    # target specific spiral level
    n = int(sqrt(target) - 1) // 2 + 1
    corner = (2 * n + 1)**2

    # find closest corner
    while corner >= target:
        corner += -2 * n
    # back off to 2nd to last corner in this spiral level
    corner += 2 * n

    # compute L1 distance to origin
    width = 2 * n + 1
    distance = max([abs(target - corner), abs(target - corner) - width // 2])

    # integer division doesn't necessarily simplify!
    L1_norm = 2 * (width // 2) - distance

    return L1_norm


# ------------- Part 2


def day_3_2017_part_2(target):
    # seems easiest to build a sufficiently large data structure in-place
    n = 100
    A = np.zeros((n, n), dtype=np.uint64)

    stencil = np.ones((3, 3), dtype=np.uint8)

    # start from center
    a, b = n // 2, n // 2
    A[a, b] = 1

    # search for target value
    for k in range(1, n // 2):
        # build spiral of indices at each level of the spiral
        idx = []
        a, b = a, b + 1
        idx.append([a, b])

        # queue up all locations in array to be set
        width = 2 * k + 1
        for i in range(width - 2):
            a, b = a - 1, b
            idx.append([a, b])
        for i in range(width - 1):
            a, b = a, b - 1
            idx.append([a, b])
        for i in range(width - 1):
            a, b = a + 1, b
            idx.append([a, b])
        for i in range(width - 1):
            a, b = a, b + 1
            idx.append([a, b])

        # sequence is successive application of 2D convolutions
        # not most efficient, but hey its terse
        for a, b in idx:
            value = (stencil * A[a - 1: a + 2, b - 1: b + 2]).sum()
            if value > target:
                return value
            A[a, b] = value


# Tests ----------------------------------------------


@pytest.mark.parametrize("method, inp, expected", [
    (day_3_2017_part_1, 1, 0),
    (day_3_2017_part_1, 12, 3),
    (day_3_2017_part_1, 23, 2),
    (day_3_2017_part_1, 1024, 31),

    (day_3_2017_part_2, 130, 133),
    (day_3_2017_part_2, 200, 304),
])
def test_day_3_2017_cases(method, inp, expected):
    assert method(inp) == expected


if __name__ == '__main__':
    # show solution
    main_inp = 265149
    print("day_3_2017_part_1 solution:", day_3_2017_part_1(main_inp))
    print("day_3_2017_part_2 solution:", day_3_2017_part_2(main_inp))

    # run verification tests
    pytest.main(['-x', '-l', __file__])
