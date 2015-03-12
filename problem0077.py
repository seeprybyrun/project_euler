# It is possible to write ten as the sum of primes in exactly five
# different ways:
# 
# 7 + 3
# 5 + 5
# 5 + 3 + 2
# 3 + 3 + 2 + 2
# 2 + 2 + 2 + 2 + 2
# 
# What is the first value which can be written as the sum of primes
# in over five thousand different ways?

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
# for denominations of all prime amounts from 1 up to n

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
    index = '{0},{1}'.format(target,m)
    if index in memo:
        return memo[index]

    # ways of making change for target using coins 1 through m is
    # equal to the number of ways of making change using only coins
    # 1 through m-1 PLUS the number of ways of making change for
    # target-m using coins 1 through m
    memo[index] = makeChange(target,denoms[:-1]) + makeChange(target-m,denoms)

    return memo[index]

nt.allPrimesLessThan2(100) # workaround to initialize prime list
                           # (otherwise there is a bug)

beatThis = 5000

# increment target until we beat the desired amount
target = 10
numWays = 0
while numWays <= beatThis:
    target += 1
    denoms = nt.allPrimesLessThan2(target)
    # print denoms
    numWays = makeChange(target,denoms)
    # print 'numWays({}) = {}'.format(target,numWays)

answer = target

print 'answer: {}'.format(answer) # 71
print 'seconds elapsed: {}'.format(time.clock()-t0) # ~9.6ms
