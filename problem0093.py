# -*- coding: utf-8 -*-
# By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and
# making use of the four arithmetic operations (+, −, *, /) and
# brackets/parentheses, it is possible to form different positive integer
# targets.
# 
# For example,
# 
# 8 = (4 * (1 + 3)) / 2
# 14 = 4 * (3 + 1 / 2)
# 19 = 4 * (2 + 3) − 1
# 36 = 3 * 4 * (2 + 1)
# 
# Note that concatenations of the digits, like 12 + 34, are not allowed.
# 
# Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different
# target numbers of which 36 is the maximum, and each of the numbers 1 to 28
# can be obtained before encountering the first non-expressible number.
# 
# Find the set of four distinct digits, a < b < c < d, for which the longest
# set of consecutive positive integers, 1 to n, can be obtained, giving your
# answer as a string: abcd.
    
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
    if n % 3 > 1 or n % 4 > 1 or (n%16 not in [0,1,4,9]): return False
    sqrtN = int(floor(sqrt(n)))
    return sqrtN**2 == n

answer = ''
t0 = time.clock()

def computeSolution(a,b,c,d,op1,op2,op3,precedence):
    if precedence == 0:
        return op3(op2(op1(a,b),c),d)
    elif precedence == 1:
        return op1(a,op2(b,op3(c,d)))
    elif precedence == 2:
        return op3(op1(a,op2(b,c)),d)
    elif precedence == 3:
        return op1(a,op3(op2(b,c),d))
    elif precedence == 4:
        return op2(op1(a,b),op3(c,d))

def customDiv(a,b):
    if b == 0:
        return float('nan')
    elif a % b != 0:
        return 1.0*a/b
    else:
        return a/b

ops = [operator.add,operator.sub,operator.mul,customDiv]
bestRun = 0

# first attempt: brute force!
# (10!/6!) permutations * 4^3 operator choices * 5 precedences ~ 1.6e6 iterations
for a,b,c,d in it.combinations(range(10),4):
    results = []
    run = -1
    for a,b,c,d in it.permutations([a,b,c,d]):
        for op1,op2,op3 in it.product(ops,repeat=3):
            for precedence in range(5):
                s = computeSolution(a,b,c,d,op1,op2,op3,precedence)
                if not math.isnan(s) and s % 1 == 0:
                    results.append(int(s))

    results = sorted([x for x in set(results) if x >= 1])

    # easy skip
    if 1 not in results:
        continue

    # compute the longest run of ints from 1 onward
    for i,x in enumerate(results):
        if x != i+1:
            run = i
            break
    if run < 0:
        run = max(results)

    # check for best run so far
    if run > bestRun:
        bestRun = run
        answer = ''.join(map(str,sorted([a,b,c,d])))
        #print a,b,c,d,'---',run,results

print 'answer: {}'.format(answer) # 1258
print 'seconds elapsed: {}'.format(time.clock()-t0) # ~2.82 s
