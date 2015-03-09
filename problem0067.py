import time
import math
import numbertheory as nt
import itertools as it
from fractions import gcd
from copy import copy

from math import floor,sqrt

t0 = time.clock()
answer = -1

##triangle = [ [3],
##             [7,4],
##             [2,4,6],
##             [8,5,9,3] ]

f = open('p067_triangle.txt')
triangle = [ map(int,line.split()) for line in f.readlines() ]

N = len(triangle)
thisRowBest = [triangle[0][0]+triangle[1][0],
               triangle[0][0]+triangle[1][1]]

#dynamicprogramming
for i in range(2,N):
    prevRowBest = copy(thisRowBest)
    thisRowBest = [prevRowBest[0] + triangle[i][0]]
    thisRowBest += [max(prevRowBest[j-1],prevRowBest[j]) + triangle[i][j] for j in range(1,i)]
    thisRowBest += [prevRowBest[i-1] + triangle[i][i]]

answer = max(thisRowBest)

print 'answer: {}'.format(answer)
print 'seconds elapsed: {}'.format(time.clock()-t0)
