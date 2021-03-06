# The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
# 
# Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

import time
import math
import numbertheory as nt

t0 = time.clock()

def powMod(b,x,m):
    out = 1
    for i in range(x):
        out *= b
        out %= m
    return out

mod = 10000000000
tot = 0
for i in range(1,1001):
    tot += powMod(i,i,mod)
    tot %= mod

print 'answer: {0}'.format(tot)
print 'milliseconds elapsed: {0}'.format(1000*(time.clock()-t0))
