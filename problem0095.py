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

answer = inf
longestChainLength = 0
t0 = time.clock()

# naive method: compute all chains for integers 4 <= n <= 999999
# let f(n) = smallest integer in the amicable chain for n;
#   if n is prime or has an element >= 10**6, f(n) = inf
# let g(n) = length of amicable chain containing n;
#   if n is prime or has an element >= 10**6, g(n) = -inf
# then compute f(n) for any n with maximal g(n)

sopd = nt.sumOfProperDivisors
MAX = 10**6
chainComputed = [False for _ in range(MAX)]
chainComputed[0] = True
chainComputed[1] = True

tLast = t0

for n in range(2,MAX):

    if n % (MAX/100) == 0:
        tNew = time.clock()
        print n,tNew-tLast,tNew-t0
        tLast = tNew
    
    if chainComputed[n]: continue
    
    n1 = sopd(n)
    chain = [n,n1]
    #print n,n1,
    chainComputed[n] = True
    # iteratively compute the next element of the chain
    while n1 != n:
        if n1 >= MAX: # this kills everything previously computed in the chain
            for k in chain[:-1]:
                chainComputed[k] = True
            break

        n1 = sopd(n1)
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

print 'answer: {}'.format(answer) # 
print 'seconds elapsed: {}'.format(time.clock()-t0) # ~ 
