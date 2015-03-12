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

# memoization to improve performance
memo = {}

def makeChange(target,denoms):
    # base cases
    if target == 0:
        return 1
    elif target < 0:
        return 0
    elif len(denoms) == 0:
        return 0

    m = max(denoms)
    index = '{},{}'.format(target,m)
    if index in memo:
        return memo[index]

    # ways of making change for target using coins 1 through m is
    # equal to the number of ways of making change using only coins
    # 1 through m-1 PLUS the number of ways of making change for
    # target-m using coins 1 through m
    numWays1 = 0
    if '{},{}'.format(target,m-1) in memo:
        numWays1 = memo['{},{}'.format(target,m-1)]
    else:
        print 'recursive call: {},{}'.format(target,m-1)
        numWays1 = makeChange(target,denoms[:-1])

    numWays2 = 0
    if '{},{}'.format(target-m,m) in memo:
        numWays2 = memo['{},{}'.format(target-m,m)]
    else:
        print 'recursive call: {},{}'.format(target-m,m)
        numWays2 = makeChange(target-m,denoms)
        
    memo[index] = numWays1 + numWays2
    return memo[index]

# increment target until we beat the desired amount
target = 0
denoms = []
numWays = 1
while numWays % 10**6 != 0:
    target += 1
    denoms += [target]
    # print denoms
    numWays = makeChange(target,denoms)
    if target % 100 == 0: print target
    print 'numWays({}) = {}'.format(target,numWays)

answer = target

print 'answer: {}'.format(answer) # 71
print 'seconds elapsed: {}'.format(time.clock()-t0) # ~9.6ms
