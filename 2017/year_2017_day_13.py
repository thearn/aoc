"""Day 13: 'title' https://adventofcode.com/2017/day/13."""

import pytest
from collections import defaultdict
maxint = 10000000
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
configs = main_inp.split("\n")
main_inp = []

"""
caught: any number congruent to depth mod (2 * (rnge - 1)).
"""

max_depth = 0
for step in configs:
    depth, rnge = step.split(": ")
    depth, rnge = int(depth), int(rnge)
    main_inp.append([depth, rnge])
# Part 1 ---------------------------------


def day_13_2017_part_1(fw, delay = 0, fail_fast=False):
    """Part 1."""

    severity = 0
    for depth, rnge in fw:
        if (delay + depth) % (2 * (rnge - 1)) == 0 :
            if fail_fast:
                return False
            severity += depth * rnge

    if fail_fast and severity == 0:
        return True
    return severity

# Part 2 --------------------------------


def day_13_2017_part_2(configs):
    """Part 2."""
    i = 0
    for i in range(maxint):
        if day_13_2017_part_1(configs, delay=i, fail_fast=True):
            return i
        i += 1


# Tests ---------------------------------


test_1 = """0: 3
1: 2
4: 4
6: 4"""
configs = test_1.split("\n")
test_1 = []

max_depth = 0
for step in configs:
    depth, rnge = step.split(": ")
    depth, rnge = int(depth), int(rnge)
    test_1.append([depth, rnge])
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
    print('day_13_2017_part_2 solution:', day_13_2017_part_2(main_inp))

    # run verification tests
    pytest.main(['-x', '-l', __file__])
