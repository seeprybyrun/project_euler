# -*- coding: utf-8 -*-
# It turns out that 12 cm is the smallest length of wire that can be bent to
# form an integer sided right angle triangle in exactly one way, but there
# are many more examples.
# 
# 12 cm: (3,4,5)
# 24 cm: (6,8,10)
# 30 cm: (5,12,13)
# 36 cm: (9,12,15)
# 40 cm: (8,15,17)
# 48 cm: (12,16,20)
# 
# In contrast, some lengths of wire, like 20 cm, cannot be bent to form an
# integer sided right angle triangle, and other lengths allow more than one
# solution to be found; for example, using 120 cm it is possible to form
# exactly three different integer sided right angle triangles.
# 
# 120 cm: (30,40,50), (20,48,52), (24,45,51)
# 
# Given that L is the length of the wire, for how many values of L ≤ 1,500,000
# can exactly one integer sided right angle triangle be formed?

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

MAX_PERIM = 1500000

triplesByPerimeter = [0 for i in range(MAX_PERIM+1)]

kBound = MAX_PERIM/12 + 1
for k in range(1,kBound+1):
    discriminant = 2.0*MAX_PERIM/k + 1
    mBound = int(ceil( (sqrt(discriminant) - 1)/2 ))
    for m in range(2,mBound+1):
        for n in range(1,m):
            if (m - n) % 2 == 0 or gcd(m,n) > 1: continue
            p = perimeterOfTriple(m,n,k)
            if p > MAX_PERIM: break
            triplesByPerimeter[p] += 1

answer = sum([1 if triplesByPerimeter[i] == 1 else 0 for i in range(MAX_PERIM+1)])

##maxNumTriples = 0
##bestPerimeter = 0
##
##for i in range(0,MAX_PERIMETER+1,2):
###    if triplesByPerimeter[i] > 0:
###        print "{0}\t{1}".format(i,'*'*triplesByPerimeter[i])
##    if triplesByPerimeter[i] > maxNumTriples:
##        maxNumTriples = triplesByPerimeter[i]
##        bestPerimeter = i
    
print "answer: {}".format(answer)
print "seconds elapsed: {}".format(time.clock()-t0)
