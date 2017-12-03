import os, shutil

year, day = 2015, 4

for day in range(2, 26):
    orig = '_template.py'
    dst = '%d/year_%d_day_%d.py' % (year, year, day)
    if not os.path.exists(dst):
        with open(orig, 'r') as f:
            code = f.read()

        code = code.replace('Day 2', 'Day %d' % day)
        code = code.replace('/2017/day/2.', '/%d/day/%d.' % (year, day))
        code = code.replace('day_2_part', 'day_%d_%d_part' % (day, year), 100)

        with open(dst, 'w') as f:
            f.write(code)