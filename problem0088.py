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

    def updateX(x,i):
        x[-i] += 1
        for j in range(1,i):
            x[-j] = x[-i]
        return x

    def doStuff(x,n,mostRecentlyChanged,last1Index):
        # remove the 1s from the front to form xPrime
        xPrime = tuple(x[last1Index+1:])

        # if there were too many ones, iterate
        if len(xPrime) <= 1:
            x[-1] += 1
                    
        else:
            if xPrime not in kValues:
                k = findK(xPrime)
                kValues[xPrime] = k
                if k <= maxK:
                    p = sum(xPrime) + k - len(xPrime)
                    minProdSumNum[k] = min(minProdSumNum[k],p)
            else:
                k = kValues[xPrime]
                
            if k <= maxK:
                x[-1] += 1
            else:
                y = x[mostRecentlyChanged]
                # walk backward until you find a term that is 2 below y
                for i in range(mostRecentlyChanged-1,-1,-1):
                    if x[i] >= y-1: continue
                    else: break
                # then increase that term by 1 and set all later terms equal to it
                x[i] += 1
                for j in range(i+1,n):
                    x[j] = x[i]

        # check that no terms are above k
        i = 1
        while x[-i] > n and i < len(x):
            i += 1
            x = updateX(x,i)
        mostRecentlyChanged = n-i

        while last1Index >= 0 and x[last1Index] > 1:
            last1Index -= 1

        return x,mostRecentlyChanged,last1Index

    minProdSumNum = [inf for i in range(maxK+1)]
    minProdSumNum[1] = 1 # 1 = 1
    kValues = dict()

    x = [1] * n
    mostRecentlyChanged = n-1
    last1Index = n-1
    while x[0] < n or set(x) == {n}:
        x,mostRecentlyChanged,last1Index = doStuff(x,n,mostRecentlyChanged,last1Index)

    return minProdSumNum

# start script here
t0 = time.clock()
answer = 0
maxK = 12000
maxTupleLen = 2000
minProdSumNum = findKForNTuplesUpTo(maxTupleLen,maxK)

answer = sum(set(minProdSumNum[2:]))
if answer == inf:
    numInf = 0
    for i in range(2,maxK):
        if minProdSumNum[i] == inf:
            numInf += 1
    print 'numInf = {}, %Inf = {}'.format(numInf,100.*numInf/(maxK-1))

print 'answer: {}'.format(answer) # 
print 'seconds elapsed: {}'.format(time.clock()-t0) # ~
