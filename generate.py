import os, shutil

year, day = 2017, 4

orig = '_template.py'
dst = '%d/year_%d_day_%d.py' % (year, year, day)
if not os.path.exists(dst):
    with open(orig, 'r') as f:
        code = f.read()

    code = code.replace('Day 2', 'Day %d' % day)
    code = code.replace('/2017/day/2.', '/%d/day/%d.' % (year, day))
    code = code.replace('day_2_part', 'day_%d_part' % day, 100)

    with open(dst, 'w') as f:
        f.write(code)