"""Day 14: 'title' https://adventofcode.com/2017/day/14."""

import pytest
import numpy as np
from scipy.signal import convolve2d
from scipy.ndimage import label

from year_2017_day_10 import day_10_2017_part_2

# Part 1 ---------------------------------

def day_14_2017_part_1(seq):
    """Part 1."""
    ones = 0
    for i in range(128):
        hex_data = day_10_2017_part_2("%s-%d" % (seq, i))
        bin_data = "{0:020b}".format(int(hex_data, 16))
        ones += sum([1 for i in bin_data if i == '1'])

    return ones


# Part 2 --------------------------------


def day_14_2017_part_2(seq):
    """Part 2."""
    data = []
    for i in range(128):
        hex_data = day_10_2017_part_2("%s-%d" % (seq, i))

        bin_data = "{0:020b}".format(int(hex_data, 16))
        if len(bin_data) < 128:
            bin_data = (128 - len(bin_data))*"0" + bin_data
        data.append([int(i) for i in bin_data])

    _, n = label(np.array(data, np.int))
    return n

# Tests ---------------------------------

test_1 = 'flqrgnkx'
@pytest.mark.parametrize('method, inp, expected', [
    (day_14_2017_part_1, test_1, 8108),
    (day_14_2017_part_2, test_1, 1242),
])
def test_day_14_2017_cases(method, inp, expected):
    """Test both parts."""
    assert method(inp) == expected


if __name__ == '__main__':
    # show solution
    main_inp = 'nbysizxe'
    print('day_14_2017_part_1 solution:', day_14_2017_part_1(main_inp))
    print('day_14_2017_part_2 solution:', day_14_2017_part_2(main_inp))

    # run verification tests
    pytest.main(['-x', '-l', __file__])
