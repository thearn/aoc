

cdef int genAnext(int prev):
    return (prev * 16807) % 2147483647

cdef int genBnext(int prev):
    return (prev * 48271) % 2147483647

def day_15_2017_part_1(start):
    """Part 1."""
    cdef int a = start[0]
    cdef int b = start[1]
    cdef int score = 0
    cdef int i = 0
    for i in range(40000000):
        a = genAnext(a)
        b = genBnext(b)
        if not ((a % 65536) ^ (b % 65536)):
            score += 1
    return score


cdef long genAnext_part2(long prev):
    cdef long next_a = prev
    while True:
        next_a = ( next_a * 16807) % 2147483647
        if next_a & 3 == 0:
            return next_a

cdef long genBnext_part2(long prev):
    cdef long next_b = prev
    while True:
        next_b = (next_b * 48271) % 2147483647
        if next_b & 7 == 0:
            return next_b

def day_15_2017_part_2(start):
    """Part 2."""

    cdef long a = start[0]
    cdef long b = start[1]
    score = 0
    cdef long i = 0
    for i in range(5*1000000):
        a = genAnext_part2(a)
        b = genBnext_part2(b)
        if not ((a % 65536) ^ (b % 65536)):
            score += 1
    return score
