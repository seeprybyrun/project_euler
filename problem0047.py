# -*- coding: utf-8 -*-
# The first two consecutive numbers to have two distinct prime factors are:
# 
# 14 = 2 × 7
# 15 = 3 × 5
# 
# The first three consecutive numbers to have three distinct prime factors
# are:
# 
# 644 = 2^2 × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
# 
# Find the first four consecutive integers to have four distinct prime
# factors. What is the first of these numbers?

import time
import math
import numbertheory as nt

t0 = time.clock()

n = 1000000
target = 4
numPrimeFactors = [0]*n # 0 means unchecked, -1 means prime
answer = -1

for d in range(2,n):
    if numPrimeFactors[d] == target: # check for possible win
        if [numPrimeFactors[x] for x in range(d,d+target)] == [target]*target:
            answer = d
            break

    if numPrimeFactors[d] > 0: # if composite
        continue # skip any nonprime divisors
    else:
        numPrimeFactors[d] = -1 # declare d to be prime

    for k in range(2*d,n,d): # continue the sieve
        numPrimeFactors[k] += 1

print 'answer: {0}'.format(answer)
print 'milliseconds elapsed: {0}'.format(1000*(time.clock()-t0))
