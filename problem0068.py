# Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6,
# and each line adding to nine.
# 
# Working clockwise, and starting from the group of three with the numerically
# lowest external node (4,3,2 in this example), each solution can be described
# uniquely. For example, the above solution can be described by the set:
# 4,3,2; 6,2,1; 5,1,3.
# 
# It is possible to complete the ring with four different totals: 9, 10, 11,
# and 12. There are eight solutions in total.
# 
# Total	Solution Set
# 9	4,2,3; 5,3,1; 6,1,2
# 9	4,3,2; 6,2,1; 5,1,3
# 10	2,3,5; 4,5,1; 6,1,3
# 10	2,5,3; 6,3,1; 4,1,5
# 11	1,4,6; 3,6,2; 5,2,4
# 11	1,6,4; 5,4,2; 3,2,6
# 12	1,5,6; 2,6,4; 3,4,5
# 12	1,6,5; 3,5,4; 2,4,6
# By concatenating each group it is possible to form 9-digit strings; the
# maximum string for a 3-gon ring is 432621513.
# 
# Using the numbers 1 to 10, and depending on arrangements, it is possible to
# form 16- and 17-digit strings. What is the maximum 16-digit string for a
# "magic" 5-gon ring?

import time
import math
import numbertheory as nt
import itertools as it
from fractions import gcd
from copy import copy

from math import floor,sqrt

t0 = time.clock()
answer = -1

##a + b + c == k
##d + e + b == k
##f + g + e == k
##h + i + g == k
##j + c + i == k

for x in it.permutations(range(1,11),5):
    b,e,g,i,c = x
    notChosen = set(range(1,11)) - set(x)
    for a in notChosen:
        remaining = copy(notChosen)
        remaining.remove(a)
        k = a+b+c
        for m in [k-b-e,k-e-g,k-g-i,k-i-c]:
            if m not in remaining:
                break
            remaining.remove(m)
        if len(remaining) == 0:
            outerNodes = [a,k-b-e,k-e-g,k-g-i,k-i-c]
            innerNodes = [[b,c],[e,b],[g,e],[i,g],[c,i]]
            startIndex = outerNodes.index(min(outerNodes))
            s = ''
            for offset in range(0,5):
                s += '{}{}{}'.format(outerNodes[(startIndex-offset)%5],
                                     innerNodes[(startIndex-offset)%5][0],
                                     innerNodes[(startIndex-offset)%5][1])
                if len(s) == 16 and int(s) > answer:
                    answer = int(s)

print 'answer: {}'.format(answer)
print 'seconds elapsed: {}'.format(time.clock()-t0)
