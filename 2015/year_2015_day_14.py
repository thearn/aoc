"""Day 14: 'title' https://adventofcode.com/2015/day/14."""

import pytest


# Part 1 ---------------------------------


def day_14_2015_part_1(n):
    """Part 1."""
    return 0


# Part 2 --------------------------------


def day_14_2015_part_2(n):
    """Part 2."""
    return 0


# Tests ---------------------------------


@pytest.mark.skip(reason='Not completed yet.')
@pytest.mark.parametrize('inp, expected, method', [
    (day_14_2015_part_1, 0, 0),
    (day_14_2015_part_2, 0, 0),
])
def test_day_2_cases(inp, expected, method):
    """Test both parts."""
    assert method(inp) == expected


if __name__ == '__main__':
    # show solution
    main_inp = 0
    print('day_14_2015_part_1 solution:', day_14_2015_part_1(main_inp))
    print('day_14_2015_part_2 solution:', day_14_2015_part_2(main_inp))

    # run verification tests
    pytest.main(['-x', '-l', __file__])
