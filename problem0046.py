import time
import math
import numbertheory as nt

t0 = time.clock()

PRIMEBOUND = 6000
SQBOUND = 80

canBeWritten = [False] * PRIMEBOUND

primes = nt.allPrimesLessThan(PRIMEBOUND)

print 'done computing primes'

squares = [i**2 for i in range(SQBOUND)]

for p in primes:
    for s in squares:
        if p+2*s < len(canBeWritten):
            canBeWritten[p+2*s] = True

print 'done sieving'

for i in range(3,len(canBeWritten),2):
    if not canBeWritten[i]:
        print 'cannot be written as p + 2s^2: {0}'.format(i)

print 'milliseconds elapsed: {0}'.format(1000*(time.clock()-t0))
