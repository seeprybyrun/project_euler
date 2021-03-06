# -*- coding: utf-8 -*-
# Euler's Totient function, φ(n) [sometimes called the phi function], is
# used to determine the number of numbers less than n which are relatively
# prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine
# and relatively prime to nine, φ(9)=6.
# 
# n	Relatively Prime	φ(n)	n/φ(n)
# 2	1	                1	2
# 3	1,2	                2	1.5
# 4	1,3	                2	2
# 5	1,2,3,4	                4	1.25
# 6	1,5	                2	3
# 7	1,2,3,4,5,6	        6	1.1666...
# 8	1,3,5,7	                4	2
# 9	1,2,4,5,7,8	        6	1.5
# 10	1,3,7,9	                4	2.5
#
# It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.
# 
# Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.

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
answer = -1
bestRatio = 0

# phi(n) = n*prod_{p|n}(1-1/p)
# n/phi(n) = prod_{p|n} p/(p-1)

##MAX = 100
##primes = nt.allPrimesLessThan2(MAX+1)
##N = len(primes)
##for i in range(2**N):
##    s = bin(i)[2:]
##    s = '0'*(N-len(s)) + s
##    print s
##    n = 1
##    ratio = 1.0
##    for j in range(N):
##        if s[j] == '1':
##            n *= primes[j]
##            ratio *= primes[j]/(primes[j]-1.0)
##        if n > MAX: break
##    if n > MAX: continue
##    if ratio > bestRatio:
##        answer = n
##        bestRatio = ratio

MAX = 100000
#unchecked = set(range(2,MAX+1))
primes = nt.allPrimesLessThan2(MAX+1)
N = len(primes)
#maxPowers = [int(floor(log(MAX)/log(p))) for p in primes]
#maxPowers = [1 for p in primes]
powers = [1,1] + [0] * (N-2)
n = 6
highestPrime = 3
numChecked = 0

##print maxPowers

while highestPrime <= MAX/2:
    if n <= MAX:
##        print n
        numChecked += 1
        phi = nt.totient(powers)
        ratio = 1.0*n/phi
        if ratio > bestRatio:
            bestRatio = ratio
            answer = n
##        unchecked -= set([n])
        if numChecked % 1000 == 0:
            print '{} numbers left'.format(MAX - numChecked)
        # increment the powers
        powers[0] += 1
        n *= 2
        for i in range(N):
            if powers[i] > 1:#maxPowers[i]:
                n /= primes[i]**powers[i]
                powers[i] = 0
                n *= primes[i+1]
                powers[i+1] += 1
                if powers[i+1] == 1 and primes[i+1] > highestPrime:
                    highestPrime = primes[i+1]
##                    print highestPrime
                    n /= 2**(powers[0]-1)
                    n = int(n)
                    powers[0] = 1 # can skip any primes since their ratio will be close to 1
                    break
            else:
                break
    else:
##        print n,'skipped'
        for i,p in enumerate(primes):
            n /= p**powers[i]
            powers[i] = 0
            n *= primes[i+1]
            powers[i+1] += 1
            if powers[i+1] == 1 and primes[i+1] > highestPrime:
                highestPrime = primes[i+1]
##                print highestPrime
                break
            if n < MAX:
                break

print 'answer: {},{}'.format(answer,bestRatio)
print 'seconds elapsed: {}'.format(time.clock()-t0)
