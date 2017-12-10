"""Day 4: 'The Ideal Stocking Stuffer' https://adventofcode.com/2015/day/4."""

import pytest
import hashlib

def md5(string):
    return hashlib.md5(string.encode('utf-8')).hexdigest()


# Part 1 ---------------------------------


def day_4_2015_part_1(key, n_zeroes=5):
    """Part 1."""
    start = 0
    while True:
        string = key + str(start)
        code = md5(string)
        if code[:n_zeroes] == n_zeroes*'0':
            return start
        start += 1


# Part 2 --------------------------------


def day_4_2015_part_2(key):
    """Part 2."""
    return day_4_2015_part_1(key, n_zeroes=6)


# Tests ---------------------------------


@pytest.mark.parametrize('method, inp, expected', [
    (day_4_2015_part_1, 'abcdef', 609043),
    (day_4_2015_part_1, 'pqrstuv', 1048970),
])
def test_day_4_2015_cases(method, inp, expected):
    """Test both parts."""
    assert method(inp) == expected


if __name__ == '__main__':
    # show solution
    main_inp = 'bgvyzdsv'
    print('day_4_2015_part_1 solution:', day_4_2015_part_1(main_inp))
    print('day_4_2015_part_2 solution:', day_4_2015_part_2(main_inp))

    # run verification tests
    pytest.main(['-x', '-l', __file__])
