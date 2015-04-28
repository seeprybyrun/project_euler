# It is easily proved that no equilateral triangle exists with integral length
# sides and integral area. However, the almost equilateral triangle 5-5-6 has
# an area of 12 square units.
# 
# We shall define an almost equilateral triangle to be a triangle for which
# two sides are equal and the third differs by no more than one unit.
# 
# Find the sum of the perimeters of all almost equilateral triangles with
# integral side lengths and area and whose perimeters do not exceed one
# billion (1,000,000,000).
    
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

answer = 0
t0 = time.clock()

# next idea: generate pythagorean triples (since the height needs to be
# integral) and count the ones that turn out to make almost-equilateral
# triangles

MAX_PERIM = 10**9
mBound = int(ceil( (sqrt(2*MAX_PERIM + 1) - 1)/2 ))

n = 1

flag = 0

for m in range(2,mBound+1):
    if 2*m*(m+n) >= MAX_PERIM: break
    if (m - n) % 2 == 0 or gcd(m,n) > 1: continue

    changed = False
    
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2 # hypotenuse
    
    if abs(2*b-c) == 1:
        #print (c,c,2*b), (m,n)
        answer += 2*(b+c)
        changed = True
    elif abs(2*a-c) == 1:
        #print (c,c,2*a), (m,n)
        answer += 2*(a+c)
        changed = True

    if changed:
        if flag == 0:
            flag = 1
        elif flag == 1:
            n = m
            flag = 0

print 'answer: {}'.format(answer) # 518408346
print 'seconds elapsed: {}'.format(time.clock()-t0) # ~ 28.6 ms
