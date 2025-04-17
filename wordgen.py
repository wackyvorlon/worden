#!/usr/bin/python3

import random

def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile, 2):
        if random.randrange(num):
            continue
        line = aline
    return line

lines = open('common-syllables.txt').read().splitlines()

myline = random.choice(lines)

numsyl = random.choice(range(5))

for i in range(numsyl):
    myline+=random.choice(lines)
    

print(myline)
