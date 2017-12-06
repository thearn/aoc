"""Day 6: 'Memory Reallocation' https://adventofcode.com/2017/day/6."""

import pytest


main_inp = "11  11  13  7   0   15  5   5   4   4   1   1   7   1   15  11"


# Part 1 ---------------------------------


def day_6_2017_part_1(config):
    """Part 1."""
    config = [int(i) for i in config.split()]
    n = len(config)
    visited = [config]
    steps = 1
    while True:
        config = visited[-1]
        idx = config.index(max(config))
        bank = config[idx]
        new_config = [i for i in config]
        new_config[idx] = 0

        for i in range(bank):
            idx += 1
            if idx == n:
                idx = 0
            new_config[idx] += 1
        if new_config in visited:
            return steps
        visited.append(new_config)
        steps += 1


# Part 2 --------------------------------


def day_6_2017_part_2(config):
    """Part 2."""
    config = [int(i) for i in config.split()]
    n = len(config)
    visited = [config]
    steps = 1
    while True:
        config = visited[-1]
        idx = config.index(max(config))
        bank = config[idx]
        new_config = [i for i in config]
        new_config[idx] = 0

        for i in range(bank):
            idx += 1
            if idx == n:
                idx = 0
            new_config[idx] += 1
        if new_config in visited:
            return day_6_2017_part_1(' '.join([str(k) for k in new_config]))
        visited.append(new_config)
        steps += 1


# Tests ---------------------------------


test_1 = '0 2 7 0'


@pytest.mark.parametrize('method, inp, expected', [
    (day_6_2017_part_1, test_1, 5),
    (day_6_2017_part_2, test_1, 4),
])
def test_day_6_2017_cases(method, inp, expected):
    """Test both parts."""
    assert method(inp) == expected


if __name__ == '__main__':
    # show solution
    print('day_6_2017_part_1 solution:', day_6_2017_part_1(main_inp))
    print('day_6_2017_part_2 solution:', day_6_2017_part_2(main_inp))

    # run verification tests
    pytest.main(['-x', '-l', __file__])
