"""Day 10: 'Knot Hash' https://adventofcode.com/2017/day/10."""

import pytest
import numpy as np


main_inp = '189,1,111,246,254,2,0,120,215,93,255,50,84,15,94,62'


# Part 1 ---------------------------------


def day_10_2017_part_1(lengths, inp_size=256):
    """Part 1."""
    # inputs and length as arrays
    inputs = np.arange(inp_size)
    lengths = np.array([int(i) for i in lengths.split(',')])
    n = inputs.size

    # initialize state
    skip = 0
    position = 0

    # process each length
    for length in lengths:
        # step is how long each jump is from one point to the next
        step = position + length

        # if block wraps around:
        # roll the array 'left', reverse block, then shift back
        if step > n:
            idx =  position
            inputs = np.roll(inputs, -idx)
            inputs[:length] = list(reversed(inputs[:length]))
            inputs = np.roll(inputs, idx)
        else:
            # otherwise, just reverse the block
            inputs[position: step] = list(reversed(inputs[position: step]))

        # increment position and skip length
        position = (position + length + skip) % n
        skip += 1

    return inputs[0] * inputs[1]


# Part 2 --------------------------------


def day_10_2017_part_2(lengths):
    """Part 2."""

    skip = 0
    position = 0
    inputs = list(range(256))
    lengths = [ord(i) for i in lengths] + [17, 31, 73, 47, 23]

    n = 256
    skip = 0
    position = 0
    for rounds in range(64):
        for length in lengths:
            step = position + length
            if step > n:
                idx =  position
                inputs = np.roll(inputs, -idx)
                inputs[:length] = list(reversed(inputs[:length]))
                inputs = np.roll(inputs, idx)
            else:
                inputs[position: step] = list(reversed(inputs[position: step]))

            position = (position + length + skip) % n
            skip += 1

    dense = []
    for i in range(16):
        group = inputs[16*i : 16*i + 16]
        val = np.bitwise_xor.reduce(group)
        dense.append("{:02x}".format(val))
    dense = ''.join(dense).strip()
    return dense


# Tests ---------------------------------

@pytest.mark.parametrize('method, inp, expected', [
    (day_10_2017_part_1, ['3,4,1,5', 5], 12),
    (day_10_2017_part_1, [main_inp], 38415),
    (day_10_2017_part_2,[''], 'a2582a3a0e66e6e86e3812dcb672a272'),
    (day_10_2017_part_2,['AoC 2017'], '33efeb34ea91902bb2f59c9920caa6cd'),
    (day_10_2017_part_2,['1,2,3'], '3efbe78a8d82f29979031a4aa0b16a9d'),
    (day_10_2017_part_2,['1,2,4'], '63960835bcdc130f0b66d7ff4f6a5a8e'),
])
def test_day_10_2017_cases(method, inp, expected):
    """Test both parts."""
    assert method(*inp) == expected


if __name__ == '__main__':
    # show solution

    print('day_10_2017_part_1 solution:', day_10_2017_part_1(main_inp))
    print('day_10_2017_part_2 solution:', day_10_2017_part_2(main_inp))

    # run verification tests
    pytest.main(['-x', '-l', __file__])
