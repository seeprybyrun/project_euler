import time
import math
import numbertheory as nt
from fractions import gcd

def choose(n,r):
    if r < 0 or r > n:
        return 0
    
    numer = 1
    denom = 1
    r = max(r,n-r)
    
    for k in range(n,r,-1): # n * (n-1) * ... * (r+1), has n-r terms
        numer *= k
        denom *= k-r
        d = gcd(numer,denom)
        if d > 1:
            numer /= d
            denom /= d
    assert denom == 1
    return numer

##assert choose(3,0) == 1
##assert choose(3,1) == 3
##assert choose(3,2) == 3
##assert choose(3,3) == 1
##assert choose(3,4) == 0
##assert choose(5,3) == 10

t0 = time.clock()

upperN = 100
lowerBound = 10**6
answer = 0

for n in range(23,upperN+1):
    upperR = n/2
    for r in range(3,upperR+1):
        if choose(n,r) > lowerBound:
            #print "{}_C_{} == {}".format(n,r,choose(n,r))
            answer += n-2*r+1 # count r,r+1,...,n-r as solutions
            break # no need to continue for this n

print 'answer: {0}'.format(answer)
print 'milliseconds elapsed: {0}'.format(1000*(time.clock()-t0))
