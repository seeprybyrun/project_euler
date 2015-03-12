# It is possible to write five as a sum in exactly six different ways:
# 
# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1
# 
# How many different ways can one hundred be written as a sum of at
# least two positive integers?

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
answer = 0

# dynamic programming: this is essentially the making-change problem
# for denominations of all integer amounts from 1 up to n

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

target = 100
denoms = range(1,target+1)
answer = makeChange(target,denoms)-1 # subtract 1 since '100' isn't
                                     # considered a sum

print 'answer: {}'.format(answer) # 190569291
print 'seconds elapsed: {}'.format(time.clock()-t0) # ~0.021s
