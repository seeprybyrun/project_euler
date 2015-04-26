# Each of the six faces on a cube has a different digit (0 to 9) written on it;
# the same is done to a second cube. By placing the two cubes side-by-side in
# different positions we can form a variety of 2-digit numbers.
#
# For example, the square number 64 could be formed:
#    6 4
# In fact, by carefully choosing the digits on both cubes it is possible to
# display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36,
# 49, 64, and 81.
#
# For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9}
# on one cube and {1, 2, 3, 4, 8, 9} on the other cube.
# 
# However, for this problem we shall allow the 6 or 9 to be turned upside-down
# so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows
# for all nine square numbers to be displayed; otherwise it would be
# impossible to obtain 09.
# 
# In determining a distinct arrangement we are interested in the digits on
# each cube, not the order.
# 
# {1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
# {1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}
# 
# But because we are allowing 6 and 9 to be reversed, the two distinct sets in
# the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for
# the purpose of forming 2-digit numbers.
# 
# How many distinct arrangements of the two cubes allow for all of the square
# numbers to be displayed?
    
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

answer = 0
t0 = time.clock()

# for each number, one cube must have the first digit and the other must have
# the second digit
def validTriangle(x1,y1,x2,y2):
    # three possible angles can be right
    # 1. origin as base
    if x1*x2 + y1*y2 == 0: return True
    # 2. (x1,y1) as base
    if x1*(x2-x1) + y1*(y2-y1) == 0: return True
    # 3. (x2,y2) as base
    if x2*(x1-x2) + y2*(y1-y2) == 0: return True

    return False

    # x1*x2 == -y1*y2               => x1/y1 == -y2/x2
    # or x1*(x2-x1) == -y1*(y2-y1)  => x1/y1 == -(y2-y1)/(x2-x1)
    # or x2*(x1-x2) == -y2*(y1-y2)  => x2/y2 == -(y1-y2)/(x1-x2)

##assert validTriangle(1,0,0,1)
##assert validTriangle(1,1,2,0)
##assert validTriangle(2,0,1,1)
##assert validTriangle(0,2,1,1)
##assert validTriangle(1,1,0,2)
##assert not validTriangle(1,2,2,1)

MAX_X = 50
MAX_Y = 50

# first attempt: brute force!
for x1,y1 in it.product(range(MAX_X+1),range(MAX_Y+1)):
    if x1 == y1 == 0: continue
    for x2 in range(x1+1):
        if x2 < x1:
            yUpper = MAX_Y+1
        else:
            yUpper = y1
        for y2 in range(yUpper):
            if x2 == y2 == 0:
                continue
            if validTriangle(x1,y1,x2,y2):
                answer += 1

print 'answer: {}'.format(answer) # 14234
print 'seconds elapsed: {}'.format(time.clock()-t0) # ~2.96 s
