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
answer = 0

MAX = 100
memo = [[(int(floor(sqrt(n))),1,0,1,0)] for n in range(MAX+1)]

def convergentOfSqrt(n,k):
    """Returns (a,b), where a/b is the kth convergent of the continued
fraction expansion of sqrt(n)."""
    if isSquare(n) and k > 0:
        return int(floor(sqrt(n))),1
    
    if len(memo[n]) > k and memo[n][k]:
        return memo[n][k][-2],memo[n][k][-1]

    # increase the size of the list in memo to be long enough
    if len(memo[n]) <= k:
        memo[n] += [None] * (k-len(memo[n])+1)
        assert(len(memo[n])) == k+1

    if k > 0: # k == 0 is already covered
        for i in range(k):
            if not memo[n][i]:
                convergentOfSqrt(n,i)
        a,prevDenom,b,hPrev1,kPrev1 = memo[n][k-1]
        if k == 1:
            a = int(floor(sqrt(n)))
            denom = 1
            b = int(floor(sqrt(n)))
            hPrev2,kPrev2 = (0,1)
        else:
            hPrev2,kPrev2 = convergentOfSqrt(n,k-2)
            denom = (n - a**2)/prevDenom
            numer = sqrt(n) + a
            b = 0
            while numer/denom > 1:
                b += 1
                a -= denom
                numer = sqrt(n) + a
            a *= -1
        memo[n][k] = (a,denom,b,b*hPrev1+hPrev2,b*kPrev1+kPrev2)

    return memo[n][k][-2],memo[n][k][-1]

def isSquare(n):
    sqrtN = int(floor(sqrt(n)))
    if sqrtN**2 == n:
        return True
    return False

def convergentOfSqrtTimes10ToThe198(n,k):
    a,b = convergentOfSqrt(n,k)
    a *= 10**99
    return a,b

##for k in range(1,10):
##    a,b = convergentOfSqrt(5,k)
##    print 1.*a/b

assert isSquare(1)

for n in range(1,101):
    if isSquare(n): continue
    #print n
    k = 1
    prevQuotient = int(floor(sqrt(n)))
    a,b = convergentOfSqrtTimes10ToThe198(n,k)
    thisQuotient = a/b
    #print thisQuotient,thisQuotient-prevQuotient
    while abs(prevQuotient - thisQuotient) > 0:
        #print thisQuotient,thisQuotient-prevQuotient
        k += 1
        a,b = convergentOfSqrtTimes10ToThe198(n,k)
        prevQuotient,thisQuotient = thisQuotient,a/b
    answer += sum(map(int,str(thisQuotient)))

print 'answer: {}'.format(answer) # 40886
print 'seconds elapsed: {}'.format(time.clock()-t0) # ~0.141s
