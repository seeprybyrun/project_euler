# -*- coding: utf-8 -*-
# Euler's Totient function, φ(n) [sometimes called the phi function], is
# used to determine the number of positive numbers less than or equal to n
# which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are
# all less than nine and relatively prime to nine, φ(9)=6.
# 
# The number 1 is considered to be relatively prime to every positive number,
# so φ(1)=1.
# 
# Interestingly, φ(87109)=79180, and it can be seen that 87109 is a
# permutation of 79180.
# 
# Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and
# the ratio n/φ(n) produces a minimum.

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
bestRatio = float('inf')

# phi(n) = n*prod_{p|n}(1-1/p)
# n/phi(n) = prod_{p|n} p/(p-1), so having lots of primes is bad
# (since we want a _low_ ratio in this problem)

##MAX = 10**5
##primes = nt.allPrimesLessThan2(MAX)
##N = len(primes)
##n = 6
##powers = [1,1] + [0] * (N-2)
##numChecked = 0
##highestPrime = 3

##print maxPowers

##while highestPrime <= MAX/2:
##    if n <= MAX:
####        print n
##        numChecked += 1
##        phi = nt.totient(powers)
##        ratio = n/(1.0*phi)
####        unchecked -= set([n])
##        if sorted(str(phi)) == sorted(str(n)):
##            print 'n={},phi={},n/phi={}'.format(n,phi,ratio)
##            if ratio < bestRatio:
##                answer = n
##                bestRatio = ratio
##        # increment the powers
##        powers[0] += 1
##        n *= 2
##        for i in range(N):
##            if powers[i] > 1:#maxPowers[i]:
##                n /= primes[i]**powers[i]
##                powers[i] = 0
##                n *= primes[i+1]
##                powers[i+1] += 1
##                if powers[i+1] == 1 and primes[i+1] > highestPrime:
##                    highestPrime = primes[i+1]
####                    print highestPrime
##                    n /= 2**(powers[0]-1)
##                    n = int(n)
##                    powers[0] = 1 # can skip any primes since their ratio will be close to 1
##                    break
##            else:
##                break
##    else:
####        print n,'skipped'
##        for i,p in enumerate(primes):
##            n /= p**powers[i]
##            powers[i] = 0
##            n *= primes[i+1]
##            powers[i+1] += 1
##            if powers[i+1] == 1 and primes[i+1] > highestPrime:
##                highestPrime = primes[i+1]
####                print highestPrime
##                break
##            if n < MAX:
##                break

# strategy: try all products of two primes and see if any of those have
# a permuted totient

MAX = 10**9
primes = nt.allPrimesLessThan2(int(floor(2*sqrt(MAX))))
smallPrimes = [p for p in primes if p < sqrt(MAX)]
largePrimes = [p for p in primes[len(smallPrimes):]]# if p < 2*sqrt(MAX)] #if p < MAX/2]
print 'len(primes)={}'.format(len(primes))
print 'len(smallPrimes)={}'.format(len(smallPrimes))
print 'len(largePrimes)={}'.format(len(largePrimes))

##for i,p in enumerate(primes):
##    for j,q in enumerate(primes[i+1:]):
##        n = p*q
##        if n >= MAX: break
##        phi = (p-1)*(q-1)
##        ratio = n*1.0/phi
##        if ratio < bestRatio and sorted(str(n)) == sorted(str(phi)):
##            print 'n={}\tphi={}\tn/phi={}'.format(n,phi,ratio)
##            answer = n
##            bestRatio = ratio

# create list of all primes that can be multiplied with to stay under MAX
# then work backward until first permuted totient found OR until ratio is too large
for i,p in enumerate(smallPrimes[::-1]):
##    if i % (N/10) == 0: print '{} percent done'.format(100*i/N)
    testingSet = smallPrimes[i+1:] + [q for q in largePrimes if p*q < MAX]
    for q in testingSet[::-1]:
        assert sorted(testingSet,reverse=True) == testingSet[::-1]
        n = p*q
##        if n >= MAX:
##            continue
        phi = (p-1)*(q-1)
        ratio = n*1.0/phi
        if ratio >= bestRatio: break
        elif sorted(str(n)) == sorted(str(phi)):
            print 'n={}\tphi={}\tn/phi={}'.format(n,phi,ratio)
            answer = n
            bestRatio = ratio
            break

print 'answer: {},{}'.format(answer,bestRatio)
print 'seconds elapsed: {}'.format(time.clock()-t0)
