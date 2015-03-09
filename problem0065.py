import time
import math
import numbertheory as nt
import itertools as it
from fractions import gcd

t0 = time.clock()
answer = -1
convergent = 100

a,b = 0,0

for i in range(convergent,0,-1):
    k = 1
    if i % 3 == 0:
        k = 2*i/3
    elif i == 1:
        k = 2

    if i == convergent:
        a,b = k,1
    else:
        a,b = b,a # invert
        a += k*b # add k
        d = gcd(a,b)
        if d != 1:
            a /= d
            b /= d

print '{}th convergent is {}/{}'.format(convergent,a,b)

answer = sum([int(c) for c in str(a)])

print 'answer: {}'.format(answer)
print 'seconds elapsed: {}'.format(time.clock()-t0)
