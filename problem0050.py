# The prime 41, can be written as the sum of six consecutive primes:
# 
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# 
# This is the longest sum of consecutive primes that adds to a prime below
# one-hundred.
# 
# The longest sum of consecutive primes below one-thousand that adds to a
# prime, contains 21 terms, and is equal to 953.
# 
# Which prime, below one-million, can be written as the sum of the most
# consecutive primes?

import time
import math
import numbertheory as nt

t0 = time.clock()

upperBound = 1000000
primes = nt.allPrimesLessThan(upperBound)
n = len(primes)
maxLen = 2
answer = -1

for i in range(n):
    for j in range(maxLen,n-i):
        q = sum(primes[i:i+j])
        if q > upperBound:
            break
        if nt.isPrime(q):
            #print '{0} == {1}'.format(q,'+'.join(map(str,primes[i:i+j])))
            if j > maxLen:
                maxLen = j
                answer = q

print 'answer: {0}'.format(answer)
print 'milliseconds elapsed: {0}'.format(1000*(time.clock()-t0))
