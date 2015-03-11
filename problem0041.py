# We shall say that an n-digit number is pandigital if it makes use of all
# the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
# and is also prime.
# 
# What is the largest n-digit pandigital prime that exists?

import numbertheory as nt
import itertools as it
import time

t0 = time.clock()

nt.eratoSieve(7654321)

# no possible n-pandigital primes with n=1,2,3,5,6,8,9
# work backwards from largest possible solution (7654321) until a
# prime is found

oneThruN = '7654321'
perms = it.permutations(oneThruN)
for x in perms:
    p = int(''.join(x))
    if nt.isPrime(p):
        print 'largest pandigital prime: {0}'.format(p)
        break

print 'seconds elapsed: {0}'.format(time.clock()-t0)
