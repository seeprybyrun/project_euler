# -*- coding: utf-8 -*-
# It was proposed by Christian Goldbach that every odd composite number can
# be written as the sum of a prime and twice a square.
# 
# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12
# 
# It turns out that the conjecture was false.
# 
# What is the smallest odd composite that cannot be written as the sum of a
# prime and twice a square?

import time
import math
import numbertheory as nt

t0 = time.clock()

PRIMEBOUND = 6000
SQBOUND = 80

canBeWritten = [False] * PRIMEBOUND

primes = nt.allPrimesLessThan(PRIMEBOUND)

print 'done computing primes'

squares = [i**2 for i in range(SQBOUND)]

for p in primes:
    for s in squares:
        if p+2*s < len(canBeWritten):
            canBeWritten[p+2*s] = True

print 'done sieving'

for i in range(3,len(canBeWritten),2):
    if not canBeWritten[i]:
        print 'cannot be written as p + 2s^2: {0}'.format(i)

print 'milliseconds elapsed: {0}'.format(1000*(time.clock()-t0))
