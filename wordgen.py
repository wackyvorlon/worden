#!/usr/bin/python3

import random

with open("/usr/share/dict/words") as f:
    words = f.read().splitlines()
    

def makeword():
    
    lines = open('common-syllables.txt').read().splitlines()

    myline = random.choice(lines)

    numsyl = random.choice(range(3))

    for i in range(numsyl):
        myline+=random.choice(lines)

    return myline
    
myline = makeword()

if myline in words:
    myline = makeword()
    
print(myline)
