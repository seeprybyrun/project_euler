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
# It can be seen that there are 3 fractions between 1/3 and 1/2.
# 
# How many fractions lie between 1/3 and 1/2 in the sorted set of reduced
# proper fractions for d ≤ 12,000?

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
answer = 0
a1,b1 = 1,3
a2,b2 = 1,2

MAX = 12000

for d in range(4,MAX+1):
    if d % (MAX/10) == 0: print d
    # a1/b1 < n/d < a2/b2
    lowerBound = a1*d/b1 + 1
    upperBound = a2*d/b2 + 1
    numerators = [n for n in range(lowerBound,upperBound) if gcd(n,d) == 1]
    answer += len(numerators)

print 'answer: {}'.format(answer)
print 'seconds elapsed: {}'.format(time.clock()-t0)
