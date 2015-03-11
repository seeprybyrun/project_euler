# -*- coding: utf-8 -*-
# Consider the fraction, n/d, where n and d are positive integers. If n<d and
# HCF(n,d)=1, it is called a reduced proper fraction.
# 
# If we list the set of reduced proper fractions for d ≤ 8 in ascending order
# of size, we get:
# 
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3,
# 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# 
# It can be seen that 2/5 is the fraction immediately to the left of 3/7.
# 
# By listing the set of reduced proper fractions for d ≤ 1,000,000 in
# ascending order of size, find the numerator of the fraction immediately
# to the left of 3/7.

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

t0 = time.clock()
a,b = 3,7
numer,denom = 0,1

MAX = 10**6

for d in range(2,MAX+1):
    # numer/denom <= n/d < 3/7
##    lowerBound = numer*d/denom
##    upperBound = 3*d/7
    n = a*d/b
    x = 1.0*n/d
    if 1.0*numer/denom < x < 1.0*a/b:
        #print '{}/{}'.format(n,d)
        numer,denom = n,d

print 'answer: {}/{}'.format(numer,denom)
print 'seconds elapsed: {}'.format(time.clock()-t0)
