"""Day 10: 'Knot Hash' https://adventofcode.com/2017/day/10."""

import pytest
import numpy as np

# Part 1 ---------------------------------


def day_10_2017_part_1(seq):
    """Part 1."""
    inputs, lengths = seq
    inputs = np.array(inputs)
    lengths = np.array(lengths)
    n = inputs.size
    skip = 0
    position = 0

    for length in lengths:
        step = position + length
        if step > n:
            idx =  position
            inputs = np.roll(inputs, -idx)
            #print(length, "REV:", inputs, n - step)
            inputs[:length] = list(reversed(inputs[:length]))
            inputs = np.roll(inputs, idx)
        else:
            inputs[position: step] = list(reversed(inputs[position: step]))

        #print("length : %d, pos : %d, skip: %d" % (length, position, skip))
        position = (position + length + skip) % n
        skip += 1
        #print(length, inputs)

    return inputs[0] * inputs[1]


# Part 2 --------------------------------


def day_10_2017_part_2(n):
    """Part 2."""
    return 0


# Tests ---------------------------------

inp_1 = [0, 1, 2, 3, 4]
lengths_1 = [3, 4, 1, 5]
#38415

@pytest.mark.parametrize('method, inp, expected', [
    (day_10_2017_part_1, [inp_1, lengths_1], 12),
    (day_10_2017_part_2, 0, 0),
])
def test_day_10_2017_cases(method, inp, expected):
    """Test both parts."""
    assert method(inp) == expected


if __name__ == '__main__':
    # show solution
    lengths = [189,1,111,246,254,2,0,120,215,93,255,50,84,15,94,62]
    main_inp = list(range(256))
    print('day_10_2017_part_1 solution:', day_10_2017_part_1([main_inp, lengths]))
    #print('day_10_2017_part_2 solution:', day_10_2017_part_2(main_inp))

    # run verification tests
    pytest.main(['-x', '-l', __file__])
