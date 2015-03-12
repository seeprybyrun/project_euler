# It is well known that if the square root of a natural number is not an
# integer, then it is irrational. The decimal expansion of such square roots
# is infinite without any repeating pattern at all.
# 
# The square root of two is 1.41421356237309504880..., and the digital sum of
# the first one hundred decimal digits is 475.
# 
# For the first one hundred natural numbers, find the total of the digital sums
# of the first one hundred decimal digits for all the irrational square roots.

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

memo = {}

def convergentOfSqrt2(k):
    """Returns (a,b), where a/b is the kth convergent of sqrt(2), and a and b are coprime.
The 1st iteration is 3/2."""
    if k in memo:
        return memo[k]
    
    if k == 1:
        memo[1] = (3,2)
    else:
        a,b = convergentOfSqrt2(k-1)
        # add one, invert, add one
        a += b
        a,b = b,a
        a += b
        memo[k] = (a,b)

    return memo[k]

def convergentOfSqrtTimes10ToThe198(k):
    a,b = convergentOfSqrt2(k)
    a *= 10**99
    return a,b

k = 1
prevQuotient = int(floor(sqrt(2)))
a,b = convergentOfSqrt2Times10ToThe198(k)
thisQuotient = a/b
print thisQuotient,thisQuotient-prevQuotient
while abs(prevQuotient - thisQuotient) > 0:
    print thisQuotient,thisQuotient-prevQuotient
    k += 1
    a,b = convergentOfSqrt2Times10ToThe198(k)
    prevQuotient,thisQuotient = thisQuotient,a/b
answer = sum(map(int,str(thisQuotient)))

print 'answer: {}'.format(answer) # 
print 'seconds elapsed: {}'.format(time.clock()-t0) # ~
