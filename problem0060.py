# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two
# primes and concatenating them in any order the result will always be prime.
# For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of
# these four primes, 792, represents the lowest sum for a set of four primes
# with this property.
# 
# Find the lowest sum for a set of five primes for which any two primes
# concatenate to produce another prime.

import time
import math
import numbertheory as nt
import itertools as it
import string

def isPrime(n):
    if n < MAX_SIEVE:
        return nt.isPrime2(n)
    else:
        return nt.isPrimeNoSieve(n)

t0 = time.clock()
answer = 0
bestTuple = None
MAX_PRIMES = 10000
MAX_SIEVE = 10000
nt.eratoSieve2(MAX_SIEVE+1)
primes = [3] + nt.allPrimesLessThan2(MAX_PRIMES)[3:] # don't include 2 or 5
lowestSum = sum(primes[-5:])

##for x in it.combinations(primes,4):
##    if sum(x) >= lowestSum:
##        #print 'skipped {}'.format(x)
##        continue
####    xMod3 = set([q % 3 for q in x])
####    if (x[0] == 3 and len(xMod3) > 2) or (x[0] > 3 and len(xMod3) > 1):
####        continue
##    xMod3 = [q % 3 for q in x]
##    if 1 in xMod3 and 2 in xMod3:
##        continue
##    goodTuple = True
##    for y in it.permutations(x,2):
##        p = int(str(y[0]) + str(y[1]))
##        if not nt.isPrimeNoSieve(p):
##            goodTuple = False
##            break
##    if goodTuple:
##        print x
##        bestTuple = goodTuple
##        lowestSum = sum(x)

##badPrimes = {p:[] for p in primes}
##
##N = len(primes)
##for i1 in range(N):
##    p1 = primes[i1]
##    if p1 > lowestSum:
##        break
##    flag11 = (p1 % 3 == 1)
##    flag12 = (p1 % 3 == 2)
##    #print p1
##
##    for i2 in range(i1+1,N):
##        p2 = primes[i2]
##        if p1 + p2 > lowestSum:
##            break
##        flag21 = flag11 or (p2 % 3 == 1)
##        flag22 = flag12 or (p2 % 3 == 2)
##        if flag21 and flag22:
##            continue
##        if p2 in badPrimes[p1]:
##            continue
##        q = int(str(p1) + str(p2))
##        r = int(str(p2) + str(p1))
##        if not (isPrime(q) and isPrime(r)):
##            badPrimes[p1].append(p2)
##            badPrimes[p2].append(p1)
##            continue
##        #print p1,p2
##        
##        for i3 in range(i2+1,N):
##            p3 = primes[i3]
##            if p1+p2+p3 > lowestSum:
##                break
##            flag31 = flag21 or (p3 % 3 == 1)
##            flag32 = flag22 or (p3 % 3 == 2)
##            if flag31 and flag32:
##                continue
##            goodTuple = True
##            for p in [p1,p2]:
##                if p3 in badPrimes[p]:
##                    goodTuple = False
##                    break
##                q = int(str(p) + str(p3))
##                r = int(str(p3) + str(p))
##                if not (isPrime(q) and isPrime(r)):
##                    goodTuple = False
##                    badPrimes[p].append(p3)
##                    badPrimes[p3].append(p)
##                    break
##            if not goodTuple:
##                continue
##            #print p1,p2,p3
##            
##            for i4 in range(i3+1,N):
##                p4 = primes[i4]
##                if p1+p2+p3+p4 > lowestSum:
##                    break
##                flag41 = flag31 or (p4 % 3 == 1)
##                flag42 = flag32 or (p4 % 3 == 2)
##                if flag41 and flag42:
##                    continue
##                goodTuple = True
##                for p in [p1,p2,p3]:
##                    if p4 in badPrimes[p]:
##                        goodTuple = False
##                        break
##                    q = int(str(p) + str(p4))
##                    r = int(str(p4) + str(p))
##                    if not (isPrime(q) and isPrime(r)):
##                        goodTuple = False
##                        badPrimes[p].append(p4)
##                        badPrimes[p4].append(p)
##                        break
##                if not goodTuple:
##                    continue
##                print p1,p2,p3,p4
##
##                for i5 in range(i4+1,N):
##                    p5 = primes[i5]
##                    if p1+p2+p3+p4+p5 > lowestSum:
##                        break
##                    flag51 = flag41 or (p4 % 3 == 1)
##                    flag52 = flag42 or (p4 % 3 == 2)
##                    if flag51 and flag52:
##                        continue
##                    goodTuple = True
##                    for p in [p1,p2,p3,p4]:
##                        if p5 in badPrimes[p]:
##                            goodTuple = False
##                            break
##                        q = int(str(p) + str(p5))
##                        r = int(str(p5) + str(p))
##                        if not (isPrime(q) and isPrime(r)):
##                            goodTuple = False
##                            badPrimes[p].append(p5)
##                            badPrimes[p5].append(p)
##                            break
##                    if not goodTuple:
##                        continue
##
##                    print p1,p2,p3,p4,p5
##                    lowestSum = p1+p2+p3+p4+p5

N = len(primes)
nbrs = {p:set() for p in primes}

print 'building the graph'

# build the graph
for i in range(N):
    for j in range(i+1,N):
        if (primes[i] + primes[j]) % 3 == 0:
            continue
        p = int(str(primes[i])+str(primes[j]))
        q = int(str(primes[j])+str(primes[i]))
        if not (isPrime(p) and isPrime(q)):
            continue
        nbrs[primes[i]] |= set([primes[j]])

print 'searching for cliques'

# search for a clique with lowest sum
for p1 in primes:
    if p1 > lowestSum:
        break
    for p2 in nbrs[p1]:
        if p1+p2 > lowestSum:
            break
        for p3 in sorted(nbrs[p1] & nbrs[p2]):
            if p1+p2+p3 > lowestSum:
                break
            for p4 in sorted(nbrs[p1] & nbrs[p2] & nbrs[p3]):
                if p1+p2+p3+p4 > lowestSum:
                    break
                for p5 in sorted(nbrs[p1] & nbrs[p2] & nbrs[p3] & nbrs[p4]):
                    if p1+p2+p3+p4+p5 > lowestSum:
                        break
                    
                    print p1,'+',p2,'+',p3,'+',p4,'+',p5,'==',p1+p2+p3+p4+p5
                    lowestSum = p1+p2+p3+p4+p5

answer = lowestSum

##print badPrimes
        
print 'answer: {}'.format(lowestSum)
print 'seconds elapsed: {}'.format(time.clock()-t0)
