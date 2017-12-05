"""Day 1: 'title' https://adventofcode.com/2016/day/1."""

import pytest


# Part 1 ---------------------------------


def day_1_2016_part_1(seq):
    """Part 1."""
    steps = seq.split(', ')
    position = 0
    heading = 1j
    for step in steps:
        dir_letter = step[0]
        if dir_letter == "R":
            heading = heading * (-1j)
        else:
            heading = heading * 1j

        step_size = int(step[1:])
        position += step_size * heading

    return int(abs(position.imag) + abs(position.real))


# Part 2 --------------------------------


def day_1_2016_part_2(seq):
    """Part 1."""
    steps = seq.split(', ')
    position = 0
    visited = [position]
    heading = 1j
    for step in steps:
        dir_letter = step[0]
        if dir_letter == "R":
            heading = heading * (-1j)
        else:
            heading = heading * 1j

        step_size = int(step[1:])
        for i in range(step_size):
            position += heading
            if position in visited:
                return int(abs(position.imag) + abs(position.real))
            visited.append(position)


# Tests ---------------------------------


#@pytest.mark.skip(reason='Not completed yet.')
@pytest.mark.parametrize('method, inp, expected', [
    (day_1_2016_part_1, 'R2, L3', 5),
    (day_1_2016_part_1, 'R2, R2, R2', 2),
    (day_1_2016_part_1, 'R5, L5, R5, R3', 12),
    (day_1_2016_part_2, 'R8, R4, R4, R8', 4),
])
def test_day_1_2016_cases(method, inp, expected):
    """Test both parts."""
    assert method(inp) == expected


if __name__ == '__main__':
    # show solution
    main_inp = 'R3, L5, R1, R2, L5, R2, R3, L2, L5, R5, L4, L3, R5, L1, R3, R4, R1, L3, R3, L2, L5, L2, R4, R5, R5, L4, L3, L3, R4, R4, R5, L5, L3, R2, R2, L3, L4, L5, R1, R3, L3, R2, L3, R5, L194, L2, L5, R2, R1, R1, L1, L5, L4, R4, R2, R2, L4, L1, R2, R53, R3, L5, R72, R2, L5, R3, L4, R187, L4, L5, L2, R1, R3, R5, L4, L4, R2, R5, L5, L4, L3, R5, L2, R1, R1, R4, L1, R2, L3, R5, L4, R2, L3, R1, L4, R4, L1, L2, R3, L1, L1, R4, R3, L4, R2, R5, L2, L3, L3, L1, R3, R5, R2, R3, R1, R2, L1, L4, L5, L2, R4, R5, L2, R4, R4, L3, R2, R1, L4, R3, L3, L4, L3, L1, R3, L2, R2, L4, L4, L5, R3, R5, R3, L2, R5, L2, L1, L5, L1, R2, R4, L5, R2, L4, L5, L4, L5, L2, L5, L4, R5, R3, R2, R2, L3, R3, L2, L5'
    print('day_1_2016_part_1 solution:', day_1_2016_part_1(main_inp))
    print('day_1_2016_part_2 solution:', day_1_2016_part_2(main_inp))

    # run verification tests
    pytest.main(['-x', '-l', __file__])
