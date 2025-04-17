#!/usr/bin/python3

import random


lines = open('common-syllables.txt').read().splitlines()

myline = random.choice(lines)

numsyl = random.choice(range(3))

for i in range(numsyl):
    myline+=random.choice(lines)
    

print(myline)
