# By counting carefully it can be seen that a rectangular grid measuring 3 by 2
# contains eighteen rectangles.
# 
# Although there exists no rectangular grid that contains exactly two million
# rectangles, find the area of the grid with the nearest solution.

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

##def rectangleCount(m,n):
##    tot = 0
##    # count number of rectangles of size i by j
##
##    # iterative method
####    for i in range(1,m+1):
####        for j in range(1,n+1):
####            tot += (m-i+1)*(n-j+1)
##
##    # analytic method
##    # (m-i+1)(n-j+1) = mn - mj + m - ni + ij - i + n - j + 1
##    # \sum_{i=1}^m \sum_{j=1}^n mn - mj + m - ni + ij - i + n - j + 1
##    # = \sum_{i=1}^m \sum_{j=1}^n (mn + m + n + 1) - (m+1)j - (n+1)i + ij
##    # = mn(mn+m+n+1) - m(m+1) \sum_{j=1}^n j - n(n+1) \sum_{i=1}^m i + \sum_{i=1}^m i \sum_{j=1}^n j
##    # = mn(mn+m+n+1) - m(m+1)n(n+1)/2 - m(m+1)n(n+1)/2 + m(m+1)n(n+1)/4
##    return m*n*(m*n + m + n + 1) - 3*m*n*(m+1)*(n+1)/4

# if m == n, then we get
# m^2(m^2 + 2m + 1) - 3m^2(m+1)^2/4
# m^2(m+1)^2 - (3/4)m^2(m+1)^2
# m^2(m+1)^2/4
# (m(m+1)/2)^2 = (mth triangular number)^2

# so if (m(m+1)/2)^2 == TARGET, then
# m(m+1)/2 == sqrt(TARGET), so
# m^2 + m - 2*sqrt(TARGET) == 0, giving us
# m == (-1 + sqrt(1 + 8*sqrt(TARGET)))/2. (minus solution gives m < 0, so
#                                          ignore it)
# so the minimum side length for a square that has at least TARGET
# rectangles is (sqrt(1+8*sqrt(TARGET))-1)/2. So we should consider sigmas
# near the value sqrt(1+8*sqrt(TARGET))-1
#
# for a given value of m+n, maximum 

# start script here
t0 = time.clock()
answer = None
closestToTarget = inf
TARGET = 2 * 10**6 # two million
START_SIGMA = int(ceil(sqrt(1+8*sqrt(TARGET))-1))
#print START_SIGMA

for delta in sorted(range(0,START_SIGMA)+range(0,-START_SIGMA,-1),key=abs):
    sigma = START_SIGMA + delta
    for m in range(sigma/2,-1,-1): # since rectangleCount(m,n) == rectangleCount(n,m),
        n = sigma-m              # no need to consider when m > n
        r = m*n*(m*n + m + n + 1) - 3*m*n*(m+1)*(n+1)/4
        if abs(r-TARGET) < abs(closestToTarget-TARGET):
#            print m,n,r
            closestToTarget = r
            answer = m*n                                  

print 'answer: {}'.format(answer) # 2772
print 'seconds elapsed: {}'.format(time.clock()-t0) # ~15.1ms
