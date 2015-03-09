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
