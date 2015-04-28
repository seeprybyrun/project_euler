from math import sqrt
from math import floor
from math import log
from operator import mul

memo = {}
sumOfDivisorsMemo = {}
divisorsMemo = {}
genPent = [1]

def divisors(n):
    # naive method
    if n not in divisorsMemo:
        upperBound = int(floor(sqrt(n)))+1
##        divs = [i for i in range(1,upperBound) if n % i == 0]
##        divs.extend([n/i for i in divs if i*i != n])
        divs = []
        for i in range(1,upperBound):
            if n % i == 0:
                divs.append(i)
                if n/i != i:
                    divs.append(n/i)
        divisorsMemo[n] = divs
    return divisorsMemo[n]

def sumOfDivisors(n):

##    def extendGenPent(minBeforeStopping):
##        L = len(genPent)
##        if L % 2 == 0:
##            i = -L/2
##        else:
##            i = L/2 + 1
##        while True:
##            i = -i
##            if i > 0:
##                i += 1
##            p = (3*i**2 - i)/2
##            genPent.append(p)
##            if p >= minBeforeStopping:
##                break

##    # this method is slower than having a hash
##    def extendSumOfDivisorsMemo(upper):
##        L = len(sumOfDivisorsMemo)
##        if L <= upper:
##            sumOfDivisorsMemo.extend([-1] * (upper-L+1))
##
##    if len(sumOfDivisorsMemo) <= n:
##        extendSumOfDivisorsMemo(n)

    if n not in sumOfDivisorsMemo:
        
        # naive method
        sumOfDivisorsMemo[n] = sum(divisors(n))
        
##        # using Euler's recursive method... this is slower than naive!
##        sod = 0
##        if genPent[-1] < n: # genPent[-1] == max(genPent) because it's sorted
##            extendGenPent(n)
##        for i,p in enumerate(genPent):
##            if p > n: break
##            sign = 1 if (i%4<2) else -1
##            if p == n:
##                sod += sign * n
##                #print '+' if sign == 1 else '-', n,
##            else:
##                t = sumOfDivisors(n-p)
##                sod += sign * t
##                #print '+' if sign == 1 else '-', t,
##        sumOfDivisorsMemo[n] = sod
##        #print ''
        
    return sumOfDivisorsMemo[n]

assert sumOfDivisors(6) == 6*2
assert sumOfDivisors(28) == 28*2

def sumOfProperDivisors(n):
    return sumOfDivisors(n) - n

def areAmicable(a,b):
    return (a != b) and (a == sumOfProperDivisors(b)) and (b == sumOfProperDivisors(a))

def allAmicableNumbersLessThan(n):
    amicableNums = []
    for i in range(1,n):
        j = sumOfProperDivisors(i)
        if areAmicable(i,j):
            amicableNums.append(i)
    return amicableNums

def isPrimeNoSieve(n):
    rootN = int(floor(sqrt(n)))
    if memo['maxPrime'] <= rootN:
        raise Exception
    for p in allPrimesLessThan2(rootN+1):
        if n % p == 0:
            return False
    return True

def eratoSieve(m):
    n = int(floor(m))
    print 'computing sieve of Eratosthenes up through {}'.format(n)
    checked = [False]*(n+1)
    prime = [False]*(n+1)
    
    for d in range(2,n):
        if checked[d] and not prime[d]:
            continue # skip any nonprime divisors
        else:
            checked[d] = True
            prime[d] = True # declare d to be prime
        for k in range(2*d,n,d):
            checked[k] = True
            prime[k] = False
    memo['maxPrime'] = n
    memo['isPrime'] = prime

def eratoSieve2(m):
    n = int(floor(m))
    print 'computing sieve of Eratosthenes up through {}'.format(n)
    prime = [True]*(n+1)
    rootN = int(floor(sqrt(n)))
    
    for d in range(2,rootN+1):
        if prime[d]:
            for j in range(d**2,n+1,d):
                prime[j] = False
    memo['maxPrime'] = n
    memo['isPrime'] = prime

def allPrimesLessThan(m):
    n = int(floor(m))
    
    if 'maxPrime' not in memo or memo['maxPrime'] <= n:
        eratoSieve(n)
        
    if 'primes' in memo:
        return [p for p in memo['primes'] if p < n]
    
    primes = []
    for i in range(2,n):
        if isPrime(i):
            primes.append(i)
            
    memo['primes'] = primes
    return primes

def allPrimesLessThan2(m):
    n = int(floor(m))
    
    if 'maxPrime' not in memo or memo['maxPrime'] <= n:
        eratoSieve2(n)
        
    if 'primes' in memo:
        return [p for p in memo['primes'] if p < n]
        
    primes = []
    for i in range(2,n):
        if isPrime2(i):
            primes.append(i)
            
    memo['primes'] = primes
    return primes

def isPrime(n):
    if n <= 1:
        return False
    
    if 'maxPrime' in memo and memo['maxPrime'] > n:
        return memo['isPrime'][n]
    
    bits = int(floor(log(n)/log(2)) + 1)
    eratoSieve(2**bits)
    return memo['isPrime'][n]

def isPrime2(n):
    if n <= 1:
        return False
    
    if 'maxPrime' in memo and memo['maxPrime'] > n:
        return memo['isPrime'][n]
    
    bits = int(floor(log(n)/log(2)) + 1)
    eratoSieve2(2**bits)
    return memo['isPrime'][n]

##eratoSieve(100)
##for i in range(100):
##    if isPrime(i):
##        print '{0} is prime'.format(i)

def euclidExtended(x,y):
    """Returns (a,b) such that a*x + b*y == 1. Returns None if no such integers exist."""
    # special cases
    if x**2 == 1: # if x == +- 1
        return (x,0)
    if y**2 == 1: # if y == +- 1
        return (0,y)
    if x*y == 0 or x%y == 0 or y%x == 0: # if x|y or y|x
        return None
    
    switched = False
    fail = False
    
    if abs(x) > abs(y):
        x,y = y,x
        switched = True
        
    a = [1,0]
    b = [0,1]
    
    while True:
        q = x/y
        r = x%y
        a.append(a[-2]-q*a[-1])
        b.append(b[-2]-q*b[-1])
        x,y = y,r
        if r == 1:
            break
        if r == 0:
            return None

    if switched:
        return b[-1],a[-1]
    return a[-1],b[-1]

##print euclidExtended(1,1)
##print euclidExtended(2,3)
##print euclidExtended(5,3)
##print euclidExtended(2,4)
##print euclidExtended(0,1)
##print euclidExtended(1,0)
##print euclidExtended(4,6)
##print euclidExtended(-2,3)
##print euclidExtended(10,3)
##print euclidExtended(3,10)

def crt(r,m):
    """Given a list of integers r and a list of positive coprime integers m, 
returns the integer 0 <= x < N, where N is the product of the elements of m, such
that x is congruent to r[i] modulo m[i]."""
    N = reduce(mul, m, 1) #product of elements of m

    # use extended euclidean algorithm to find a,b such that a*m_i + b*m_j == 1
    # so a*m_i == 1 mod m_j, so a*m_i*r_j == r_j mod m_j
    # and b*m_j == 1 mod m_i, so b*m_j*r_i == r_i mod m_i
    # so we can take x == a*m_i*r_j + b*m_j*r_i (mod m_i*m_j)
    # then take r_i = x, m_i = m_i*m_j, and set r_j and m_j to the next ones in the list, and repeat

    r_i,m_i = r[0],m[0]
    r_i %= m_i
    
    n = len(zip(r,m))
    for j in range(1,n):
        r_j,m_j = r[j],m[j]
        a,b = euclidExtended(m_i,m_j)
        r_i = a*m_i*r_j + b*m_j*r_i
        m_i = m_i*m_j
        r_i %= m_i

    return r_i

#print crt([1,4,1],[2,17,9])

def powmod(a,b,m):
    # TODO: is this faster using the Euler totient function to reduce the exponent?
    prod = 1
    for i in range(b):
        prod *= a
        prod %= m
    return prod

def totient(primeDivisors,n=None):
    """Takes a list of the form [k_2,k_3,k_5,...] that gives
the number of powers of the ith prime dividing a number, and
outputs the totient of the number."""

    primes = []
    if n:
        primes = allPrimesLessThan2(n)
    else:
        primes = memo['primes']

    totient = 1
    for i,k in enumerate(primeDivisors):
        if k == 0: continue
        p = primes[i]
        totient *= p**k - p**(k-1)
    return totient
