

cdef int genAnext(int prev):
    return (prev * 16807) % 2147483647

cdef int genBnext(int prev):
    return (prev * 48271) % 2147483647

def day_15_2017_part_1(start):
    """Part 1."""
    cdef int a = start[0]
    cdef int b = start[1]
    cdef int score = 0
    cdef long i = 0L
    for i in range(40*1000000L):
        a = genAnext(a)
        b = genBnext(b)
        if not ((a % 65536L) ^ (b % 65536L)):
            score += 1
    return score


cdef unsigned long genAnext_part2(unsigned long prev):
    cdef unsigned long next_a = prev
    while True:
        next_a = ( next_a * 16807) % 2147483647L
        if next_a & 3 == 0:
            return next_a

cdef unsigned long genBnext_part2(unsigned long prev):
    cdef unsigned long next_b = prev
    while True:
        next_b = (next_b * 48271) % 2147483647L
        if next_b & 7 == 0:
            return next_b

def day_15_2017_part_2(start):
    """Part 2."""

    cdef unsigned long a = start[0]
    cdef unsigned long b = start[1]
    score = 0
    cdef unsigned long i = 0
    for i in range(5*1000000L):
        a = genAnext_part2(a)
        b = genBnext_part2(b)
        if not ((a % 65536) ^ (b % 65536)):
            score += 1
    return score
