# Let p(n) represent the number of different ways in which n coins can be
# separated into piles. For example, five coins can separated into piles in
# exactly seven different ways, so p(5)=7.
# 
# OOOOO
# OOOO   O
# OOO   OO
# OOO   O   O
# OO   OO   O
# OO   O   O   O
# O   O   O   O   O
# Find the least value of n for which p(n) is divisible by one million.

import time
import math
import numbertheory as nt
import itertools as it
import operator
from fractions import gcd
from copy import copy

from math import floor,sqrt,log

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

factorial = [1,1,2,6,24,120,720,5040,40320,362880]

t0 = time.clock()
answer = -1

# dynamic programming: this is essentially the making-change problem
# for denominations of all amounts from 1 up to n

maxAmount = 1
numWays = [ [1],[0,1] ]
modulus = 10**6

while answer < 0:
    maxAmount += 1
    if maxAmount % 100 == 0:
        print maxAmount 
##    # fill in new column
##    for i in range(maxAmount):
##        numWays[i] += [numWays[i][-1]]

    # make new row
    numWays.append([0] * (maxAmount+1))
    
    # ways of making change for target using coins 1 through m is
    # equal to the number of ways of making change using only coins
    # 1 through m-1 PLUS the number of ways of making change for
    # target-denoms[m] using coins 1 through m
    for m in range(1,maxAmount+1):
        numWays1 = numWays[maxAmount][m-1]
        v = maxAmount-m
        numWays2 = numWays[v][m] if v > m else numWays[v][v]
        numWays[maxAmount][m] = (numWays1 + numWays2) % modulus
    if numWays[maxAmount][maxAmount] == 0:
        answer = maxAmount

##    for row in numWays:
##        print row

print 'answer: {}'.format(answer) # 
print 'seconds elapsed: {}'.format(time.clock()-t0) # 
