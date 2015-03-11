# The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit
# number, 134217728=8^9, is a ninth power.
# 
# How many n-digit positive integers exist which are also an nth power?

import time
import math
import numbertheory as nt
import itertools as it

from math import log10
from math import floor
from math import ceil

t0 = time.clock()
answer = 0

# observation: 9**21 has 21 digits, but 9**n has fewer than n digits for n > 21
# can check this via floor(log10(9**n))+1 == floor(n*log10(9)) + 1 == n
for b in range(1,10):
    for n in range(1,22):
        numDigits = int(floor(log10(b**n))+1)
        if numDigits == n:
            #print '{}**{} == {} ({} digits)'.format(b,n,b**n,numDigits)
            answer += 1
        elif numDigits > n:
            break

print 'answer: {}'.format(answer)
print 'seconds elapsed: {}'.format(time.clock()-t0)
