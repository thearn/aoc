"""Day 2: 'title' https://adventofcode.com/2017/day/2."""

import pytest


# Part 1 ---------------------------------

def day_2_part_1(n):
    return 0


@pytest.mark.skip(reason='Not completed yet.')
@pytest.mark.parametrize('inp,expected', [
    (0, 0),
])
def test_day_2_part_1_cases(inp, expected):
    computed = day_2_part_2(inp)
    assert computed == expected


# Part 2 --------------------------------

def day_2_part_2(n):
    return 0


@pytest.mark.skip(reason='Not completed yet.')
@pytest.mark.parametrize('inp,expected', [
    (0, 0),
])
def test_day_2_part_2_cases(inp, expected):
    computed = day_2_part_2(inp)
    assert computed == expected



if __name__ == '__main__':
    # show solution
    main_inp = 0
    print('day_2_part_1 solution:', day_2_part_1(main_inp))
    print('day_2_part_2 solution:', day_2_part_2(main_inp))

    # run verification tests
    pytest.main([__file__])
