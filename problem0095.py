# The proper divisors of a number are all the divisors excluding the number
# itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As
# the sum of these divisors is equal to 28, we call it a perfect number.
# 
# Interestingly the sum of the proper divisors of 220 is 284 and the sum of
# the proper divisors of 284 is 220, forming a chain of two numbers. For this
# reason, 220 and 284 are called an amicable pair.
# 
# Perhaps less well known are longer chains. For example, starting with 12496,
# we form a chain of five numbers:
# 
# 12496 -> 14288 -> 15472 -> 14536 -> 14264 (-> 12496 -> ...)
# 
# Since this chain returns to its starting point, it is called an amicable
# chain.
# 
# Find the smallest member of the longest amicable chain with no element
# exceeding one million.
    
import time
import math
import numbertheory as nt
import itertools as it
import operator
from fractions import gcd
from copy import copy
import re
import random

from math import floor,sqrt,log,ceil,log10,exp

inf = float('inf')
factorial = [1,1,2,6,24,120,720,5040,40320,362880]

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

def printByRow(matrix):
    for row in matrix:
        print row

def isSquare(n):
    if n%3 > 1: return False
    if n%4 > 1: return False
    if n%5 in [2,3]: return False
    if n%6 in [2,5]: return False
    if n%16 not in [0,1,4,9]: return False
    
    return (sqrt(n)%1) == 0

t0 = time.clock()

MAX = 10**6
primes = nt.allPrimesLessThan2(MAX)
sopd = [-1 for _ in range(MAX)]
for p in primes:
    sopd[p] = 1

##tLast = t0
##numIterations = 1

root5N = int(floor(MAX**(0.2)))
root4N = int(floor(MAX**(0.25)))
cbrtN = int(floor(MAX**(1./3)))
sqrtN = int(floor(sqrt(MAX)))
tinyPrimes = [p for p in primes if p <= root5N]
logByTinyPrimes = [log10(MAX)/log10(p) for p in tinyPrimes]
verySmallPrimes = [p for p in primes if root5N < p <= root4N] # at most 4
minVerySmall = min(verySmallPrimes)
smallPrimes = [p for p in primes if root4N < p <= cbrtN] # at most 3
mediumPrimes = [p for p in primes if cbrtN < p <= sqrtN] # at most 2
largePrimes = [p for p in primes if sqrtN < p <= MAX/minVerySmall] # at most 1
veryLargePrimes = [p for p in primes if MAX/minVerySmall < p <= MAX/2] # can only be paired with tiny primes
superMassivePrimes = [p for p in primes if p > MAX/2] # only possible prime

##print len(tinyPrimes), tinyPrimes
##print len(verySmallPrimes), verySmallPrimes
##print len(smallPrimes), smallPrimes
##print len(mediumPrimes), mediumPrimes
##print len(largePrimes), largePrimes[:10], '...', largePrimes[-10:]
##print len(veryLargePrimes), veryLargePrimes[:10], '...', veryLargePrimes[-10:]
##print len(superMassivePrimes), superMassivePrimes[:10], '...', superMassivePrimes[-10:]

##print tinyPrimes
##print logByTinyPrimes

# compute sum of proper divisors by iterating over lists of prime factors instead of integers in order

print 'generating list of sets of large prime factors:', time.clock()-t0

bigFactorsList = []
for i in [0,1]:
    for x in it.combinations_with_replacement(largePrimes,i):
        lp = [p for p in x]
        for j in range(2-i+1):
            for y in it.combinations_with_replacement(mediumPrimes,j):
                mp = [p for p in y]
                if prod(lp + mp) >= MAX: continue
                for k in range(3-i-j+1):
                    for z in it.combinations_with_replacement(smallPrimes,k):
                        sp = [p for p in z]
                        if prod(lp + mp + sp) >= MAX: continue
                        for m in range(4-i-j-k+1):
                            for w in it.combinations_with_replacement(verySmallPrimes,m):
                                vsp = [p for p in w]
                                bf = lp + mp + sp + vsp
                                if prod(bf) >= MAX: continue
                                bigFactorsList.append(bf)
for p in veryLargePrimes:
    bigFactorsList.append([p])

#print len(bigFactorsList)

print 'computing sums of proper divisors:', time.clock()-t0

for bf in bigFactorsList:
    bigPrimes = sorted(set(bf))
    bigPowers = [bf.count(p) for p in bigPrimes]
    tinyPowers = [0 for p in tinyPrimes]
    while tinyPowers[-1] >= 0:
##        if numIterations % (MAX/10) == 0:
##            tNew = time.clock()
##            print numIterations,tNew-tLast,tNew-t0
##            tLast = tNew

        # compute sum of divisors for current set of factors and record sum of proper divisors

        if sum(tinyPowers+bigPowers) == 1:
            tinyPowers[0] += 1 # no need to worry about carry here
            continue
            
        factors = [p**k for p,k in zip(tinyPrimes+bigPrimes,tinyPowers+bigPowers)]
        # print factors
        n = prod(factors)
        if n < MAX:
            sopd[n] = prod([sum([p**j for j in range(k+1)]) for p,k in zip(tinyPrimes+bigPrimes,tinyPowers+bigPowers)]) - n
            tinyPowers[0] += 1
            mostRecentlyChanged = 0
        if n >= MAX:
            if mostRecentlyChanged == len(tinyPowers)-1:
                tinyPowers[-1] = -1
                break
            for i in range(mostRecentlyChanged+1):
                tinyPowers[i] = 0
            tinyPowers[mostRecentlyChanged+1] += 1
            mostRecentlyChanged += 1

        # update prime factorization
##        numIterations += 1
        # check for carry
        for i in range(mostRecentlyChanged,len(tinyPowers)):
            if tinyPowers[i] >= logByTinyPrimes[i]:
                if i < len(tinyPowers)-1:
                    tinyPowers[i] = 0
                    tinyPowers[i+1] += 1
                    mostRecentlyChanged = i+1
                else:
                    # end the phase
                    tinyPowers[-1] = -1
                    break
            else:
                break

# print sopd[:100]

print 'computing aliquot chains:', time.clock()-t0

chainComputed = [False for _ in range(MAX)]
chainComputed[0] = True
chainComputed[1] = True

answer = inf
longestChainLength = 0

for n in range(2,MAX):
    
    if chainComputed[n]: continue
    
    n1 = sopd[n]
    chain = [n,n1]
    #print n,n1,
    chainComputed[n] = True
    # iteratively compute the next element of the chain
    while n1 != n:
        if n1 >= MAX: # this kills everything previously computed in the chain
            for k in chain[:-1]:
                chainComputed[k] = True
            break

        n1 = sopd[n1]
        #print n1,
        if n1 != n:
            if n1 < MAX and (chainComputed[n1] or n1 in chain): # then n's chain will not get back to itself
                break
            chain.append(n1)

    #print ''
    if n1 != n: continue
    #print chain
    for k in chain:
        chainComputed[k] = True
    if len(chain) > longestChainLength:
        answer = min(chain)
        longestChainLength = len(chain)

print 'answer: {}'.format(answer) # 14316
print 'seconds elapsed: {}'.format(time.clock()-t0) # ~ 39.8 s
