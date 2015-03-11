# -*- coding: utf-8 -*-
# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.
# 
# {20,48,52}, {24,45,51}, {30,40,50}
# 
# For which value of p ≤ 1000, is the number of solutions maximised?

import time
from math import sqrt
from math import ceil
from math import floor
from fractions import gcd

def generateTriple(m,n,k):
    return (k*(m**2-n**2),k*(2*m*n),k*(m**2+n**2))

def perimeterOfTriple(m,n,k):
    # a = k*(m**2 - n**2)
    # b = k*(2*m*n)
    # c = k*(m**2 + n**2)
    # a + b + c == 2*k*m*(m+n)
    return 2*k*m*(m+n)

t0 = time.clock()

MAX_PERIMETER = 1000

triplesByPerimeter = [0 for i in range(MAX_PERIMETER+1)]

kBound = MAX_PERIMETER/12 + 1
for k in range(1,kBound+1):
    discriminant = 2.0*MAX_PERIMETER/k + 1
    mBound = int(ceil( (sqrt(discriminant) - 1)/2 ))
    for m in range(2,mBound+1):
        for n in range(1,m):
            if (m - n) % 2 == 0 or gcd(m,n) > 1: continue
            p = perimeterOfTriple(m,n,k)
            if p > MAX_PERIMETER: break
            triplesByPerimeter[p] += 1

maxNumTriples = max(triplesByPerimeter)
bestPerimeter = triplesByPerimeter.index(maxNumTriples)

##maxNumTriples = 0
##bestPerimeter = 0
##
##for i in range(0,MAX_PERIMETER+1,2):
###    if triplesByPerimeter[i] > 0:
###        print "{0}\t{1}".format(i,'*'*triplesByPerimeter[i])
##    if triplesByPerimeter[i] > maxNumTriples:
##        maxNumTriples = triplesByPerimeter[i]
##        bestPerimeter = i
    
print "total triples: {0}".format(sum(triplesByPerimeter))
print "best perimeter: {0}".format(bestPerimeter)
print "seconds elapsed: {0}".format(time.clock()-t0)
