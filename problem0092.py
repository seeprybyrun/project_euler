# -*- coding: utf-8 -*-
# A number chain is created by continuously adding the square of the digits in
# a number to form a new number until it has been seen before. For example,
# 
# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
# 
# Therefore any chain that arrives at 1 or 89 will become stuck in an endless
# loop. What is most amazing is that EVERY starting number will eventually
# arrive at 1 or 89.
# 
# How many starting numbers below ten million will arrive at 89?

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

# start script here
t0 = time.clock()
answer = 1
NUM_DIGITS = 7
MAX = 10**NUM_DIGITS
MAX_SUM = (9**2)*NUM_DIGITS # no sum of squares of digits will be larger than
                            # this

reaches = [0] * (MAX_SUM+1)
reaches[89] = 89
reaches[1] = 1

for i in range(2,MAX_SUM+1):
    # build the chain
    chain = [i]
    while True:
        r = reaches[chain[-1]]
        if r == 89:
            for j in chain[:-1]:
                reaches[j] = 89
                answer += 1
            break
        elif r == 1:
            for j in chain[:-1]:
                reaches[j] = 1
            break
        else: # terminal state not reached yet
            sumOfSquaresOfDigits = sum([int(c)**2 for c in str(chain[-1])])
            chain.append(sumOfSquaresOfDigits)
            
for i in range(MAX_SUM+1,MAX):
    x = i
    sumOfSquaresOfDigits = 0
    while x > 0: # read off each digit, square, and add to the running total
        sumOfSquaresOfDigits += (x % 10)**2
        x /= 10
    if reaches[sumOfSquaresOfDigits] == 89:
        answer += 1

print 'answer: {}'.format(answer) # 8581146
print 'seconds elapsed: {}'.format(time.clock()-t0) # ~32.0s
