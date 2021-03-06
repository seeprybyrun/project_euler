# -*- coding: utf-8 -*-
# Consider quadratic Diophantine equations of the form:
#
# x^2 – Dy^2 = 1
#
# For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.
#
# It can be assumed that there are no solutions in positive integers when D
# is square.
#
# By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the
# following:
#
# 3^2 – 2×2^2 = 1
# 2^2 – 3×1^2 = 1
# 9^2 – 5×4^2 = 1
# 5^2 – 6×2^2 = 1
# 8^2 – 7×3^2 = 1
# 
# Hence, by considering minimal solutions in x for D ≤ 7, the largest x is
# obtained when D=5.
# 
# Find the value of D ≤ 1000 in minimal solutions of x for which the largest
# value of x is obtained.

import time
import math
import numbertheory as nt
import itertools as it
from fractions import gcd

from math import floor,sqrt

t0 = time.clock()
answer = -1
bestX = -1

def isSquare(n):
    sqrtN = int(floor(sqrt(n)))
    if sqrtN**2 == n:
        return True
    return False

##def minimalX(D):
##    if isSquare(D): return None
##    y = 1
##    while not isSquare(1+D*y**2):
##        y += 1
##        if y % 100 == 0: print y
##    return int(floor(sqrt(1+D*y**2)))
##
def minimalX(D):
    if isSquare(D): return None

    a = int(floor(sqrt(D)))
    xLast,yLast = (1,0)
    xCurr,yCurr = (a,1)
    prevDenom = 1
    while True:
        if xCurr**2 - D*yCurr**2 == 1:
            return xCurr

        # find next partial denominator (b-coefficient)
        denom = (D - a**2)/prevDenom
        numer = sqrt(D) + a
        b = 0
        while numer/denom > 1:
            b += 1
            a -= denom
            numer = sqrt(D) + a
        prevDenom = denom
        a *= -1

        xLast,xCurr = xCurr,b*xCurr+xLast
        yLast,yCurr = yCurr,b*yCurr+yLast

##print 2,minimalX(2)
##print 3,minimalX(3)
##print 4,minimalX(4)
##print 5,minimalX(5)
##print 6,minimalX(6)
##print 7,minimalX(7)
##print 13,minimalX(13)

for D in range(2,1000):
    x = minimalX(D)
##    if D % 100 == 0: print D
    if x:
        if x > bestX:
            bestX = x
            answer = D

print 'answer: {},{}'.format(answer,bestX)
print 'seconds elapsed: {}'.format(time.clock()-t0)
