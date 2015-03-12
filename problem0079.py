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
answer = -1

# idea: try making a regex out of each password piece, then run
# all integers through the regexes until a match is found

f = open('data/p079_keylog.txt','r')
regexes = [re.compile('.*'+'.*'.join(str(line))+'.*') for line in f.readlines()]

answer = 10236789 # bottom of search space given that 4,5 not in keylogger
found = False
numChecked = 0
while not found:
    answer += 1
    passcode = str(answer)
    if set(passcode) != set('01236789'): # ensures that we only consider
        continue                         # passcodes with the requisite digits
    found = True
    for regex in regexes:
        if not regex.match(passcode):
            found = False
            break
    numChecked += 1
    if numChecked % 1000 == 0:
        print numChecked,passcode

print 'answer: {}'.format(answer) # 
print 'seconds elapsed: {}'.format(time.clock()-t0) # 
