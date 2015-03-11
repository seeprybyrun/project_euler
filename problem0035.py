# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.
# 
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
# 71, 73, 79, and 97.
# 
# How many circular primes are there below one million?

import numbertheory as nt
import time

def extract(n):
    return [d for d in str(n)]

def rotate(it):
    L = len(it)
    rotit = [it[(i+1)%L] for i in range(L)]
    return rotit

def recombine(digits):
    return int(''.join(digits))

def isCircular(n):
    if not nt.isPrime(n):
        return False
    nDigits = extract(n)
    pDigits = rotate(nDigits)
    p = recombine(pDigits)
    while p != n:
        if not nt.isPrime(p):
            return False
        pDigits = rotate(pDigits)
        p = recombine(pDigits)
    return True

start_time = time.clock()

upperBound = 1000000
primes = nt.allPrimesLessThan(upperBound)

checkpoint1 = time.clock()

print 'all primes less than {0} computed'.format(upperBound)
print '{0} seconds elapsed'.format(checkpoint1-start_time)

tot = 0
for p in primes:
    if isCircular(p):
        tot += 1
print 'number of circular primes: {0}'.format(tot)

end_time = time.clock()

print '{0} seconds elapsed'.format(end_time-start_time)
