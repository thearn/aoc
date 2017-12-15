"""Day 15: 'title' https://adventofcode.com/2017/day/15."""

import pytest


def genAnext(prev):
    return (prev * 16807) % 2147483647

def genBnext(prev):
    return (prev * 48271) % 2147483647

def day_15_2017_part_1(start):
    """Part 1."""
    a = start[0]
    b = start[1]
    score = 0
    for i in range(40000000):
        a, b = genAnext(a), genBnext(b)
        if not ((a % 65536) ^ (b % 65536)):
            score += 1
    return score


def genAnext_part2(prev):
    next_a = prev
    while True:
        next_a = ( next_a * 16807) % 2147483647
        if next_a & 3 == 0:
            yield next_a

def genBnext_part2(prev):
    next_b = prev
    while True:
        next_b = (next_b * 48271) % 2147483647
        if next_b & 7 == 0:
            yield next_b

def day_15_2017_part_2(start):
    """Part 2."""
    start_a, start_b = start

    a = genAnext_part2(int(start_a))
    b = genBnext_part2(int(start_b))
    score = 0
    for i in range(5*1000000):
        if not ((next(a) % 65536) ^ (next(b) % 65536)):
            score += 1
    return score


@pytest.mark.skip(reason='Not completed yet.')
@pytest.mark.parametrize('method, inp, expected', [
    (day_15_2017_part_1, 0, 0),
    (day_15_2017_part_2, 0, 0),
])
def test_day_15_2017_cases(method, inp, expected):
    """Test both parts."""
    assert method(inp) == expected


if __name__ == '__main__':
    # show solution
    main_inp = [679, 771]
    print('day_15_2017_part_1 solution:', day_15_2017_part_1(main_inp))
    print('day_15_2017_part_2 solution:', day_15_2017_part_2(main_inp))

    # run verification tests
    pytest.main(['-x', '-l', __file__])
