# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
# increases by 3330, is unusual in two ways: (i) each of the three terms are
# prime, and, (ii) each of the 4-digit numbers are permutations of one another.
# 
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
# primes, exhibiting this property, but there is one other 4-digit increasing
# sequence.
# 
# What 12-digit number do you form by concatenating the three terms in this
# sequence?

import time
import math
import numbertheory as nt

def sameDigits(x,y):
    xDigits = sorted(str(x))
    yDigits = sorted(str(y))
    return xDigits == yDigits

##print sameDigits(1,2)
##print sameDigits(10,100)
##print sameDigits(1234,4321)

t0 = time.clock()

primes = nt.allPrimesLessThan(10000)

for p in primes:
    for d in range(2,(10000-p)/2,2):
        if nt.isPrime(p+d) and nt.isPrime(p+2*d) and sameDigits(p,p+d) and sameDigits(p,p+2*d):
            print "{0},{1},{2}: {3}".format(p,p+d,p+2*d,d)
            answer = str(p)+str(p+d)+str(p+2*d)

print 'answer: {0}'.format(answer)
print 'milliseconds elapsed: {0}'.format(1000*(time.clock()-t0))
