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

# mod out by the desired target to speed up?
def makeChangeTableMod(maxAmount,denoms,modulus):
    # initialize table
    D = len(denoms)+1 # implicit null set inserted at beginning
    numWays = [ [0 for m in range(D)] for i in range(maxAmount+1) ]
    numWays[0] = [1 for m in range(D)]

    # ways of making change for target using coins 0 through m is
    # equal to the number of ways of making change using only coins
    # 0 through m-1 PLUS the number of ways of making change for
    # target-denoms[m] using coins 1 through m
    for m in range(1,D):
        d = denoms[m-1] # the minus 1 is to adjust for the previous implicit
                        # null set
        for i in range(1,maxAmount+1):
            numWays1 = numWays[i][m-1]
            numWays2 = 0 if i-d < 0 else numWays[i-d][m]
            numWays[i][m] = (numWays1 + numWays2) % modulus

    return numWays

##maxAmount = 5
##denoms = range(1,maxAmount+1)
##for row in makeChangeTable(maxAmount,denoms):
##    print row

# increment target by powers of 2 until we find one divisible by 10**6
maxAmount = 2
TARGET = 10**5
while answer < 0:
    print 'making new table: maxAmount = {}'.format(maxAmount)
    numWays = makeChangeTableMod(maxAmount,range(1,maxAmount+1),TARGET)
##    for row in numWays:
##        print row
    for i in range(maxAmount/2,maxAmount+1):
        if numWays[i][i] == 0:
            answer = i
            print 'numWays[{0}][{0}] = {1}'.format(i,numWays[i][i])
            break
    maxAmount *= 2

print 'answer: {}'.format(answer) # 
print 'seconds elapsed: {}'.format(time.clock()-t0) # 
