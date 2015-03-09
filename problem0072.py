import time
import math
import numbertheory as nt
import itertools as it
import operator
from fractions import gcd
from copy import copy

from math import floor,sqrt,log

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

t0 = time.clock()
answer = -1

# answer should be:
# \sum_{k=2}^n \phi(k) = \frac{1}{2}((\sum_{k=1}^n \mu(k) \floor{n/k}^2) - 1)
# where \mu(k) = 0 if k isn't squarefree and otherwise (-1)^{\# of distinct prime factors of k}
# so this reduces to computing the sum over all products of distinct prime factors such that the product is
#   at most n
# a prime greater than n/2 must appear by itself
# note that no two primes greater than sqrt(n) can be multiplied together
# no three primes greater than cbrt(n) can be multiplied together
# no four primes greater than n**(0.25) can be multiplied together
# etc
# since 7# (seven primorial) < 10**6 and 8# > 10**6, only need to consider products of 7 or fewer primes

MAX = 10**6
#unchecked = set(range(2,MAX+1))
primes = nt.allPrimesLessThan2(MAX+1)

t1 = time.clock()

smallerThan7thRoot = [p for p in primes      if p <= MAX**(1./7)]
primes7 = smallerThan7thRoot
n7 = len(primes7)

smallerThan6thRoot = [p for p in primes[n7:] if p <= MAX**(1./6)]
primes6 = primes7 + smallerThan6thRoot
n6 = len(primes6)

smallerThan5thRoot = [p for p in primes[n6:] if p <= MAX**(1./5)]
primes5 = primes6 + smallerThan5thRoot
n5 = len(primes5)

smallerThan4thRoot = [p for p in primes[n5:] if p <= MAX**(1./4)]
primes4 = primes5 + smallerThan4thRoot
n4 = len(primes4)

smallerThan3rdRoot = [p for p in primes[n4:] if p <= MAX**(1./3)]
primes3 = primes4 + smallerThan3rdRoot
n3 = len(primes3)

smallerThan2ndRoot = [p for p in primes[n3:] if p <= sqrt(MAX)]
primes2 = primes3 + smallerThan2ndRoot
n2 = len(primes2)

smallerThanHalf =    [p for p in primes[n2:] if p <= MAX/2]
primesHalf = primes2 + smallerThanHalf

smallerThanSixth =   [p for p in primes[n2:] if p <= MAX/6]
primesSixth = primes2 + smallerThanSixth

smallerThan30th =    [p for p in primes[n2:] if p <= MAX/30]
primes30th = primes2 + smallerThan30th

smallerThan210th =   [p for p in primes[n2:] if p <= MAX/210]
primes210th = primes2 + smallerThan210th

smallerThan2310th =  [p for p in primes[n2:] if p <= MAX/2310]
primes2310th = primes2 + smallerThan2310th

smallerThan30030th = [p for p in primes[n2:] if p <= MAX/30030]
primes30030th = primes2 + smallerThan30030th

print '0 primes: 1'
print '1 prime: {}'.format(len(primes))
print '2 primes: {}*{}'.format(n2,len(primesHalf))
print '3 primes: {}*{}*{}'.format(n3,n2,len(primesSixth))
print '4 primes: {}*{}*{}*{}'.format(n4,n3,n2,len(primes30th))
print '5 primes: {}*{}*{}*{}*{}'.format(n5,n4,n3,n2,len(primes210th))
print '6 primes: {}*{}*{}*{}*{}*{}'.format(n6,n5,n4,n3,n2,len(primes2310th))
print '7 primes: {}*{}*{}*{}*{}*{}*{}'.format(n7,n6,n5,n4,n3,n2,len(primes30030th))

# first do mu(1)
answer += MAX**2

# single primes (ALL the primes, not just primes1)
for p in primes:
    x = p
##    print x
    answer -= (MAX/x)**2

# double primes (at least one must be <= n**1/2 in size)
for i2,p2 in enumerate(primes2):
    for p1 in primesHalf[i2+1:]:
        x = p2*p1
        if x > MAX: break
##        print x
        answer += (MAX/x)**2

# triple primes (at least one must be <= small, at least two must be <= large)
for i3,p3 in enumerate(primes3):
    for i2,p2 in enumerate(primes2[i3+1:]):
        if p3*p2 > MAX: break
        for p1 in primesSixth[i3+i2+2:]:
            x = p3*p2*p1
            if x > MAX: break
##            print x
            answer -= (MAX/x)**2

# quad primes (at least one must be <= smaller, two <= medium, three <= large):
for i4,p4 in enumerate(primes4):
    for i3,p3 in enumerate(primes3[i4+1:]):
        if p4*p3 > MAX: break
        for i2,p2 in enumerate(primes2[i4+i3+2:]):
            if p4*p3*p2 > MAX: break
            for p1 in primes30th[i4+i3+i2+3:]:
                x = p4*p3*p2*p1
                if x > MAX: break
##                print x
                answer += (MAX/x)**2

# five primes
for i5,p5 in enumerate(primes5):
    for i4,p4 in enumerate(primes4[i5+1:]):
        if p5*p4 > MAX: break
        for i3,p3 in enumerate(primes3[i5+i4+2:]):
            if p5*p4*p3 > MAX: break
            for i2,p2 in enumerate(primes2[i5+i4+i3+3:]):
                if p5*p4*p3*p2 > MAX: break
                for p1 in primes210th[i5+i4+i3+i2+4:]:
                    x = p5*p4*p3*p2*p1
                    if x > MAX: break
##                    print x
                    answer -= (MAX/x)**2

# six primes
for i6,p6 in enumerate(primes6):
    for i5,p5 in enumerate(primes5[i6+1:]):
        if p6*p5 > MAX: break
        for i4,p4 in enumerate(primes4[i6+i5+2:]):
            if p6*p5*p4 > MAX: break
            for i3,p3 in enumerate(primes3[i6+i5+i4+3:]):
                if p6*p5*p4*p3 > MAX: break
                for i2,p2 in enumerate(primes2[i6+i5+i4+i3+4:]):
                    if p6*p5*p4*p3*p2 > MAX: break
                    for p1 in primes2310th[i6+i5+i4+i3+i2+5:]:
                        x = p6*p5*p4*p3*p2*p1
                        if x > MAX: break
##                        print x
                        answer += (MAX/x)**2

# seven primes
for i7,p7 in enumerate(primes7):
    for i6,p6 in enumerate(primes6[i7+1:]):
        if p7*p6 > MAX: break
        for i5,p5 in enumerate(primes5[i7+i6+2:]):
            if p7*p6*p5 > MAX: break
            for i4,p4 in enumerate(primes4[i7+i6+i5+3:]):
                if p7*p6*p5*p4 > MAX: break
                for i3,p3 in enumerate(primes3[i7+i6+i5+i4+4:]):
                    if p7*p6*p5*p4*p3 > MAX: break
                    for i2,p2 in enumerate(primes2[i7+i6+i5+i4+i3+5:]):
                        if p7*p6*p5*p4*p3*p2 > MAX: break
                        for p1 in primes30030th[i7+i6+i5+i4+i3+i2+6:]:
                            x = p7*p6*p5*p4*p3*p2*p1
                            if x > MAX: break
##                            print x
                            answer -= (MAX/x)**2

answer /= 2

t2 = time.clock()

print 'answer: {}'.format(answer)
print 'seconds elapsed: {}'.format(t2-t0)
print '(not including sieve): {}'.format(t2-t1)
