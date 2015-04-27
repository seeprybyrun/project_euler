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

# The triangles under consideration have side lengths a,a,a+-1, where
# 1 < a <= 333333333.
# The height of the triangle is given by
#   (a+-1)^2/4 + h^2 == a^2
#   (a^2 +- 2a + 1)/4 + h^2 == 4a^2/4
#   h = sqrt(3a^2 -+ 2a - 1)/2
# The area is: b*h/2 = (a+-1) * sqrt(3a^2 -+ 2a - 1) / 4
# This is integral iff 3a^2 -+ 2a - 1 is square AND
# (either 3a^2 -+ 2a - 1 is divisible by 4 and (a+-1) is even
#      or (a+-1) is divisible by 4)
# Regarding divisibility, in the former case:
#   mod 4, we want -a^2 + 2a - 1 == 0, or a^2 == 2a-1.
#   Both a == 1 mod 4 and 3 mod 4 satisfy this equation, and it also makes
#   both a+1 and a-1 even.
# In the latter case:
#   If we require a-1 == 0 mod 4, then a == 1 mod 4. If we require a+1 == 0
#   mod 4, then a == 3 mod 4. (Either way, 3a^2 -+ 2a + 1 is divisible by 4.)
# Either way, it's necessary that a == 1 or 3 mod 4, so a must be odd.
#
# Regarding squaredness, we need -+ 2a - 1 == 0 or 1 mod 3.
# In the + case: we need a-1 == 0 or 1 mod 3, so a != 0 mod 3.
# In the - case: we need -a-1 == 0 or 1 mod 3, so a != 0 mod 3.
# So a must be odd and may not be a multiple of 3.

##numIterations = 0
##a = 3
##while a < 333333333:
##    a += 2
##    if a % 3 == 0: continue
##    if isSquare(3*a**2 + 2*a - 1): # (a,a,a-1) is good
##        answer += 3*a - 1
##    if isSquare(3*a**2 - 2*a - 1): # (a,a,a+1) is good
##        answer += 3*a + 1
##    numIterations += 1
##    if numIterations % 100000 == 0:
##        print a

# Other direction:
# A = (a+b) * sqrt(3a^2 - 2ab - 1) / 4, where b == -1 or 1
# let's consider all squares s, and determine if there is an integral
# solution to s = 3a^2 - 2ab + 1
#   3a^2 - 2ab - 1-s == 0
#   a == (2b +- sqrt(4+12(1+s)))/6
#   a == (2b +- 2sqrt(4+3s))/6 == (b +- sqrt(4+3s))/3
# if 4+3s is square, then check if
#   sqrt(4+3s) % 3 == -1: if so, (a,a,a+1) is good, where a = (1+sqrt(4+3s))/3
#   sqrt(4+3s) % 3 ==  1: if so, (a,a,a-1) is good, where a = (-1+sqrt(4+3s))/3
# range on s to check:
#   (-1+sqrt(4+3s))/3 <= 333333333
#   sqrt(4+3s) <= 10**9
#   4+3s <= 10**18
#   s <= (10**18-4)/3
# so sqrt(s) <= sqrt((10**18-4)/3)

##n = 2
##UPPER = sqrt((10**18-4)/3.0)
##while n <= UPPER:
##    n += 1
##    s = n**2
##    if isSquare(4+3*s):
##        t = int(sqrt(4+3*s))
##        if t % 3 == 1:
##            a = (-1+t)/3
##            print (a,a,a-1)
##            answer += 3*a-1
##        elif t % 3 == 2:
##            a = (1+t)/3
##            print (a,a,a+1)
##            answer += 3*a+1

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

print 'answer: {}'.format(answer) # 
print 'seconds elapsed: {}'.format(time.clock()-t0) # ~
