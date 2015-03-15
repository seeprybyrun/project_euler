# A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and
# a fly, F, sits in the opposite corner. By travelling on the surfaces of the
# room the shortest "straight line" distance from S to F is 10 and the path is
# shown on the diagram (see http://projecteuler.net/problem=86)
# 
# However, there are up to three "shortest" path candidates for any given
# cuboid and the shortest route doesn't always have integer length.
# 
# It can be shown that there are exactly 2060 distinct cuboids, ignoring
# rotations, with integer dimensions, up to a maximum size of M by M by M,
# for which the shortest route has integer length when M = 100. This is the
# least value of M for which the number of solutions first exceeds two
# thousand; the number of solutions when M = 99 is 1975.
# 
# Find the least value of M such that the number of solutions first exceeds
# one million.

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

# Suppose a cuboid has side lengths a <= b <= c, where a,b,c are positive
# integers. We work out the three candidate paths between opposite corners
# confined to the surface of the cuboid.
# We'll assume the a-side lies parallel to the x-axis, the b-side to the y-
# axis, and the c-side to the z-axis.
#
# Path 1: on ab-side to b-edge, then on bc-side
# Path 2: on ac-side to c-edge, then on bc-side
# Path 3: on ab-side to a-edge, then on bc-side
#
# Suppose the path goes from the spider's corner (the origin) to point x on
# the relevant axis, then goes to the fly's corner (a,b,c). The path is then:
# Path 1: (0,0,0) to (a,x,0) to (a,b,c)
# Path 2: (0,0,0) to (a,0,x) to (a,b,c)
# Path 3: (0,0,0) to (x,b,0) to (a,b,c)
# and the distances are:
# Path 1: sqrt(a^2 + x^2) + sqrt((x-b)^2+c^2)
# Path 2: sqrt(a^2 + x^2) + sqrt((x-c)^2+b^2)
# Path 3: sqrt(b^2 + x^2) + sqrt((x-a)^2+c^2)
#
# Taking their derivatives and setting equal to 0 to get the optimal x:
# P1': x/sqrt(a^2+x^2) + (x-b)/sqrt((x-b)^2+c^2) = 0
# solutions: x1 = ab/(a-c), x2 = ab/(a+c)
# P2': x/sqrt(a^2+x^2) + (x-c)/sqrt((x-c)^2+b^2) = 0
# solutions: x1 = ac/(a-b), x2 = ac/(a+b)
# P3': x/sqrt(b^2+x^2) + (x-a)/sqrt((x-a)^2+c^2) = 0
# solutions: x1 = ab/(b-c), x2 = ab/(b+c)
# In each case, only x2 > 0, so the shortest path is given by plugging in x2
# for all three cases, and then finding the minimum of the 3 distances
# P1(ab/(a+c)) = sqrt( (a+c)^2 + b^2 )
# P2(ac/(a+b)) = sqrt( (a+b)^2 + c^2 )
# P3(ab/(b-c)) = sqrt( (b+c)^2 + a^2 )

def shortestCuboidPathSquared(a,b,c):
    assert a > 0
    assert a <= b <= c
##    d1 = (a+c)**2 + b**2
##    d2 = (a+b)**2 + c**2
##    d3 = (b+c)**2 + a**2
##    return min(d1,d2,d3)
    # when does each one win?
    # (a+c)^2 + b^2 < (a+b)^2 + c^2
    # a^2 + 2ac + c^2 + b^2 < a^2 + 2ab + b^2 + c^2
    # 2ac < 2ab
    # c < b
    # c < b iff d1 < d2
    # since b <= c, d2 <= d1
    # similarly, (a+b)^2 + c^2 > (b+c)^2 + a^2
    # a^2 + 2ab + b^2 + c^2 > b^2 + 2bc + c^2 + a^2
    # 2ab > 2bc
    # a > c iff d2 > d3
    # since a <= c, d2 <= d3
    # so d2 is always the smallest
    return (a+b)**2 + c**2

def isSquare(n):
    if n % 3 > 1 or n % 4 > 1 or (n%16 not in [0,1,4,9]): return False
    sqrtN = int(floor(sqrt(n)))
    return sqrtN**2 == n

# squares mod 8: 0,1,4,1,0,...
# squares mod 16: 0,1,4,9,0,9,4,1,0,...

# start script here
t0 = time.clock()
answer = 0
TARGET = 10**6
numIntegerSolutions = [0]
M = 0

# numIntegerSolutions[M] = numIntegerSolutions[M-1] +
#   \sum_{a=1}^M \sum_{b=a}^M 1_{isSquare((a+b)**2+M**2))} =
# numIntegerSolutions[M-1] + \sum_{s=2}^{2M} r(s) 1_{isSquare(s**2+M**2))}
while numIntegerSolutions[M] < TARGET:
    M += 1
    numIntegerSolutions.append(numIntegerSolutions[-1])
    # find s such that s**2+M**2 is square
    # there are r ways of writing s as a sum of two integers a+b, 1<=a,b<=M
    # there are M ways of writing M+1, 1 way of writing 2M and 1 way of
    # writing 2
    # so the function is:
    # r(s) = s-1 if s <= M+1, 2M-s+1 if s > M+1
    # but then, accounting for order: if r is odd, take (r+1)/2
    # if r is even, take r/2
    for s in range(2,2*M+1):
        r = s-1 if s <= M+1 else 2*M-s+1
        r = (r+1)/2 if r%2 == 1 else r/2
        numIntegerSolutions[M] += (r if isSquare(s**2+M**2) else 0)
##    print M,numIntegerSolutions[M],1.*numIntegerSolutions[M]/M**2

answer = M

print 'answer: {}'.format(answer) # 1818
print 'seconds elapsed: {}'.format(time.clock()-t0) # ~4.66s
