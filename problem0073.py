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
