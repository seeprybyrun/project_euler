# A common security method used for online banking is to ask the user for
# three random characters from a passcode. For example, if the passcode was
# 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected
# reply would be: 317.
# 
# The text file, keylog.txt, contains fifty successful login attempts.
# 
# Given that the three characters are always asked for in order, analyse the
# file so as to determine the shortest possible secret passcode of unknown
# length.

import time
import math
import numbertheory as nt
import itertools as it
import operator
from fractions import gcd
from copy import copy
import re

from math import floor,sqrt,log

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

factorial = [1,1,2,6,24,120,720,5040,40320,362880]

t0 = time.clock()
answer = None

# idea: to speed up the search, take permutations of '10236789' + extraDigits
# as needed, discarding any beginning with '0'

# send all perms of '10236789' through regex 1, dump those that don't match
# then send the survivors through regex 2, etc
# if no survivors after a regex, try extraDigits = '0', then '1', then '2', ...

f = open('data/p079_keylog.txt','r')
regexStrings = ['.*'+'.*'.join(line.strip())+'.*' for line in f.readlines()]
regexes = [re.compile(s) for s in regexStrings]

baseDigits = '01236789'
numExtraDigits = 0

while not answer:
    for x in it.combinations('01236789',numExtraDigits):
        digitStr = baseDigits + ''.join(map(str,x))
##        print digitStr
        # skip any strings that start with '0'
        candidates = set([''.join(map(str,y)) for y in it.permutations(digitStr) if y[0] != '0'])
##        print -1,len(candidates)
        for i,r in enumerate(regexes):
            survivors = set()
            for passcode in candidates:
                if r.match(passcode):
                    survivors.add(passcode)
            candidates = survivors
##            print i,len(candidates)
            if len(candidates) == 0:
                break
        if len(candidates) > 0:
            if len(candidates) == 1:
                answer = list(candidates)[0]
            else:
                answer = list(candidates)
            break
    numExtraDigits += 1

print 'answer: {}'.format(answer) # 73162890
print 'seconds elapsed: {}'.format(time.clock()-t0) # ~0.134s
