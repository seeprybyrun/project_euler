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
