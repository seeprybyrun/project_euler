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
