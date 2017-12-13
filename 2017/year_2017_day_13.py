"""Day 13: 'title' https://adventofcode.com/2017/day/13."""

import pytest
from collections import defaultdict

main_inp = """0: 3
1: 2
2: 4
4: 6
6: 5
8: 6
10: 6
12: 4
14: 8
16: 8
18: 9
20: 8
22: 6
24: 14
26: 12
28: 10
30: 12
32: 8
34: 10
36: 8
38: 8
40: 12
42: 12
44: 12
46: 12
48: 14
52: 14
54: 12
56: 12
58: 12
60: 12
62: 14
64: 14
66: 14
68: 14
70: 14
72: 14
80: 18
82: 14
84: 20
86: 14
90: 17
96: 20
98: 24"""


# Part 1 ---------------------------------


def day_13_2017_part_1(seq):
    """Part 1."""
    fw = {}
    configs = seq.split("\n")
    max_depth = 0
    for step in configs:
        depth, rnge = step.split(": ")
        depth, rnge = int(depth), int(rnge) - 1
        fw[depth] = rnge
        if depth > max_depth:
            max_depth = depth
    states = [0 for i in range(max_depth + 1)]
    directions = [-1 for i in range(max_depth + 1)]

    severity = 0
    for time_step in range(1, max_depth + 1):

        # update scanner
        for depth in fw:
            if states[depth] >= fw[depth] or states[depth] == 0:
                directions[depth] *= -1
            states[depth] = states[depth] + directions[depth]

            if states[depth] == 0 and depth == time_step:
                severity += (fw[depth] + 1) * depth

    return severity

# Part 2 --------------------------------


def day_13_2017_part_2(seq):
    """Part 2."""
    fw = {}
    configs = seq.split("\n")
    max_depth = 0
    for step in configs:
        depth, rnge = step.split(": ")
        depth, rnge = int(depth), int(rnge) - 1
        fw[depth] = rnge
        if depth > max_depth:
            max_depth = depth
    states = [0 for i in range(max_depth + 1)]
    directions = [-1 for i in range(max_depth + 1)]

    severity = 0
    for time_step in range(1, max_depth + 1):

        # update scanner
        for depth in fw:
            if states[depth] >= fw[depth] or states[depth] == 0:
                directions[depth] *= -1
            states[depth] = states[depth] + directions[depth]

            if states[depth] == 0 and depth == time_step:
                severity += (fw[depth] + 1) * depth

    return severity


# Tests ---------------------------------


test_1 = """0: 3
1: 2
4: 4
6: 4"""
@pytest.mark.parametrize('method, inp, expected', [
    (day_13_2017_part_1, test_1, 24),
    (day_13_2017_part_2, test_1, 10),
])
def test_day_13_2017_cases(method, inp, expected):
    """Test both parts."""
    assert method(inp) == expected


if __name__ == '__main__':
    # show solution
    print('day_13_2017_part_1 solution:', day_13_2017_part_1(main_inp))
    #print('day_13_2017_part_2 solution:', day_13_2017_part_2(main_inp))

    # run verification tests
    pytest.main(['-x', '-l', __file__])
