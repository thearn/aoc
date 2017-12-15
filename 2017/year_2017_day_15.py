"""Day 15: 'title' https://adventofcode.com/2017/day/15."""

import pytest

from year_2017_day_15_lib import day_15_2017_part_1, day_15_2017_part_2

main_inp = [679, 771]

@pytest.mark.parametrize('method, inp, expected', [
    (day_15_2017_part_1, main_inp, 610),
    (day_15_2017_part_2, main_inp, 306),
])
def test_day_15_2017_cases(method, inp, expected):
    """Test both parts."""
    assert method(inp) == expected


if __name__ == '__main__':
    # show solution
    print('day_15_2017_part_1 solution:', day_15_2017_part_1(main_inp))
    print('day_15_2017_part_2 solution:', day_15_2017_part_2(main_inp))

    # run verification tests
    pytest.main(['-x', '-l', __file__])
