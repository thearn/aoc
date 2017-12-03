"""Day 4: 'Inverse Captcha' https://adventofcode.com/2017/day/4."""

import pytest


def day_4_part_1(n):
    return 0


@pytest.mark.parametrize("inp,expected", [
    (1212, 0),
])
def test_day_4part_1_cases(inp, expected):
    computed = day_4_part_1(inp)
    assert computed == expected

if __name__ == '__main__':
    # show solution
    main_inp = 10
    print("Day 4.1 solution:", day_4_part_1(main_inp))

    # run verification tests
    pytest.main([__file__])
