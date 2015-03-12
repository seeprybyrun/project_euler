# Let p(n) represent the number of different ways in which n coins can be
# separated into piles. For example, five coins can separated into piles in
# exactly seven different ways, so p(5)=7.
# 
# OOOOO
# OOOO   O
# OOO   OO
# OOO   O   O
# OO   OO   O
# OO   O   O   O
# O   O   O   O   O
# Find the least value of n for which p(n) is divisible by one million.

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

factorial = [1,1,2,6,24,120,720,5040,40320,362880]

t0 = time.clock()
answer = -1

MODULUS = 10**6

# let's try Euler's recurrence:
# p(k) = \sum_{m \in S} (-1)^m p(k-P_m),
# where S = (1,-1,2,-2,3,-3,...), P_m = m(3m-1)/2 (generalized pentagonal
# numbers), and taking p(0) = 1 and p(x) = 0 for x < 0
partitions = [1]
k = 0

while partitions[k] % MODULUS != 0:
    k += 1
    m = 1
    Pm = 1
    partitions.append(0)
    while k-Pm >= 0:
        sign = 2*(m % 2)-1 # 1 if m is odd, -1 if m is even
        partitions[k] += sign * partitions[k-Pm] # the recurrence
        partitions[k] %= MODULUS # since we're only interested in the first 
                                 # one divisible by MODULUS, can use this
                                 # to keep the size of our numbers controlled
        m *= -1
        m += 0 if m < 0 else 1 # increment if we just made m positive
                               # this gives us the sequence (1,-1,2,-2,...)
        Pm = m*(3*m-1)/2 # generalized pentagonal number

answer = k

print 'answer: {}'.format(answer) # 55374
print 'seconds elapsed: {}'.format(time.clock()-t0) # ~20.2s
