# -*- coding: utf-8 -*-
# A natural number, N, that can be written as the sum and product of a given
# set of at least two natural numbers, {a1, a2, ... , ak} is called a
# product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.
# 
# For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.
# 
# For a given set of size, k, we shall call the smallest N with this property
# a minimal product-sum number. The minimal product-sum numbers for sets of
# size, k = 2, 3, 4, 5, and 6 are as follows.
# 
# k=2: 4 = 2 × 2 = 2 + 2
# k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
# k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
# k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
# k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6
# 
# Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is
# 4+6+8+12 = 30; note that 8 is only counted once in the sum.
# 
# In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is
# {4, 6, 8, 12, 15, 16}, the sum is 61.
# 
# What is the sum of all the minimal product-sum numbers for 2≤k≤12000?

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

# 2*2*3 = 12, 2+2+3 = 7, 12-7 = 5 ==> k=5+3=8
# 3*4   = 12, 3+4 = 7, 12-7 = 5 ==> k=5+2=7
# 2*6   = 12, 2+6 = 8, 12-8 = 4 ==> k=4+2=6
# given a product, can determine the k that corresponds to that product
def findK(factors):
    numOnes = prod(factors) - sum(factors)
    k = len(factors) + numOnes
    return k

# search space: lists of two or more factors > 1
# idea: do lexicographically sorted tuples of length 2 up until (2,2)
#                                          of length 3 up until (3,3,3)
#                                          of length 4 up until (4,4,4,4)
#                                          etc.
# drop any 1s that appear in the beginning of the tuple
# [2,2]
# [1,2,3] (really [2,3]) -> [1,3,3] (really [3,3]) -> [2,2,2] -> [2,2,3] ->
#   [2,3,3] -> [3,3,3]
# [1,1,2,4] -> [1,1,3,4] -> [1,1,4,4] -> [1,2,2,4] -> [1,2,3,4] -> [1,2,4,4] ->
#   [1,3,3,4] -> [1,3,4,4] -> [1,4,4,4] -> [2,2,2,2] -> [2,2,2,3] -> [2,2,2,4]
#   -> [2,2,3,3] -> [2,2,3,4] -> [2,2,4,4] -> [2,3,3,3] -> [2,3,3,4] ->
#   [2,3,4,4] -> [2,4,4,4] -> [3,3,3,3] -> [3,3,3,4] -> [3,3,4,4] -> [3,4,4,4]
#   -> [4,4,4,4]

def findKForNTuplesUpTo(n,maxK):
    # can we generate them in an order so that if we get too big, we can
    # hit a break statement and skip a lot of redundant work?
    # if findK([2,2,2,2,2]) is too high, then will findK([2,2,2,2,3]) be too high too?
    # a1*...*am - (a1+...+am) = numOnes. findK = m+numOnes
    # a1*...*am - (a1+...+am) > maxK - m =>? a1*...*(am+1) - (a1+...+am+1) > maxK - m
    # Rewriting the left side of the second inequality gives:
    # a1*...*am - (a1+...+am) + a1*...*a_{m-1} - 1 > maxK - m
    # (since a1*...*a_{m-1} > 1)
    # so the answer is yes. similarly for replacing am with am+n for any n >= 0.

    def doStuff(x,n,last1Index,mostRecentlyChanged):
        # remove the 1s from the front to form xPrime
        xPrime = tuple(x[last1Index+1:])
                    
        p = prod(xPrime)
        if p <= 2*maxK:
            numOnes = p - sum(xPrime)
            k = len(xPrime) + numOnes
            if k <= maxK:
                minProdSumNum[k] = min(minProdSumNum[k],p)
            
        if p < 2*maxK:
            x[-1] += 1
            mostRecentlyChanged = n-1
        else:
            while prod(x) >= 2*maxK:
                if mostRecentlyChanged == 0:
                    x = [n] * n
                    break
                a = x[mostRecentlyChanged-1] + 1
                for i in range(mostRecentlyChanged-1,len(x)):
                    x[i] = a
                mostRecentlyChanged -= 1
                
            while last1Index >= 0 and x[last1Index] > 1:
                last1Index -= 1

        return x,last1Index,mostRecentlyChanged

    minProdSumNum = [2*k for k in range(maxK+1)]

    x = [1]*(n-2) + [2,2]
    last1Index = n-3
    numIters = 0
    mostRecentlyChanged = n-2
    while x[0] < n:
##        numIters += 1
##        if numIters % 1000 == 0:
##            print numIters, x
        x,last1Index,mostRecentlyChanged = doStuff(x,n,last1Index,mostRecentlyChanged)

    return minProdSumNum

# start script here
t0 = time.clock()
answer = 0
maxK = 12000
tupleLen = 15 # Guaranteed to complete since every composite number n
                 # can be made into a sum-product number by taking
                 # p*(n/p)*1^(n-n/p-p) == p + n/p + 1*(n-n/p-p),
                 # where p is a prime factor of p. This gives
                 # k == n-n/p-p + 2. Taking p >= 2 gives
                 # k <= n-n/2-2 + 2 == n/2.
minProdSumNum = findKForNTuplesUpTo(tupleLen,maxK)

answer = sum(set(minProdSumNum[2:]))
if answer == inf:
    numInf = 0
    for i in range(2,maxK):
        if minProdSumNum[i] == inf:
            numInf += 1
    print 'numInf = {}, %Inf = {}'.format(numInf,100.*numInf/(maxK-1))

print 'answer: {}'.format(answer) # 7587457
print 'seconds elapsed: {}'.format(time.clock()-t0) # ~0.825s
