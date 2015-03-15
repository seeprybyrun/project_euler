# The smallest number expressible as the sum of a prime square, prime cube,
# and prime fourth power is 28. In fact, there are exactly four numbers below
# fifty that can be expressed in such a way:
# 
# 28 = 2^2 + 2^3 + 2^4
# 33 = 3^2 + 2^3 + 2^4
# 49 = 5^2 + 2^3 + 2^4
# 47 = 2^2 + 3^3 + 2^4
# 
# How many numbers below fifty million can be expressed as the sum of a prime
# square, prime cube, and prime fourth power?

import time
import math
import numbertheory as nt
import itertools as it
import operator
from fractions import gcd
from copy import copy
import re
import random

from math import floor,sqrt,log,ceil

inf = float('inf')
factorial = [1,1,2,6,24,120,720,5040,40320,362880]

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

def printByRow(matrix):
    for row in matrix:
        print row

def isSquare(n):
    if n % 3 > 1 or n % 4 > 1 or (n%16 not in [0,1,4,9]): return False
    sqrtN = int(floor(sqrt(n)))
    return sqrtN**2 == n

# start script here
t0 = time.clock()
answer = 0
MAX = 5*10**7 # 50 million

# Let MAX be the maximum number we're trying to express as a sum of prime
# powers. Let P2 be the set of primes whose squares we will consider, P3 the
# set of primes whose cubes we will consider, and P4 the set of primes whose
# fourth powers we will consider. Then 
# all primes in P2 must be at most sqrt(MAX - 2^3 - 2^4)
# all primes in P3 must be at most (MAX - 2^2 - 2^4)^(1/3)
# all primes in P4 must be at most (MAX - 2^2 - 2^3)^(1/4)
P2 = nt.allPrimesLessThan2( sqrt(MAX - 2**3 - 2**4) )
P3 = nt.allPrimesLessThan2( (MAX - 2**2 - 2**4)**(1./3) )
P4 = nt.allPrimesLessThan2( (MAX - 2**2 - 2**3)**(1./4) )

answer = len(set([p**2+q**3+r**4 for p,q,r in it.product(P2,P3,P4) if p**2+q**3+r**4 < MAX]))

print 'answer: {}'.format(answer) # 1097343
print 'seconds elapsed: {}'.format(time.clock()-t0) # ~1.53s
