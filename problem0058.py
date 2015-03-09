import time
import math
import numbertheory as nt

def cornerNumsInSpiralSquare(layer):
    ##1             1
    ##3,5,7,9       3 (+2 each)
    ##13,17,21,25   5 (+4 each)
    ##31,37,43,49   7 (+6 each)

    if layer == 1:
        return [1]

    prevCorner = (2*layer-3)**2
    corners = [prevCorner + 2*(i+1)*(layer-1) for i in range(4)]
    return corners

##def computePercentPrime(nums):
##    isPrime = nt.isPrime
##    numPrimes = sum([1.0 if isPrime(n) else 0.0 for n in nums])
##    return numPrimes/len(nums)

##print cornerNumsInSpiralSquare(1)
##print cornerNumsInSpiralSquare(2)
##print cornerNumsInSpiralSquare(3)
##print cornerNumsInSpiralSquare(4)

# first corner: i == 0
## (2*layer-3)**2 + 2*(layer-1)
## 4*layer**2 - 12*layer + 9 + (2*layer - 2)
## 4*layer**2 - 10*layer + 7
# mod 3: layer**2 - layer + 1
# layer == 2 gives 4 - 2 + 1 == 0
# if layer == 2 mod 3, then 3 | first corner
# mod 7: -3*layer**2 - 3*layer
# if layer == 0 mod 7, then 7 | first corner

# second corner: i == 1
## (2*layer-3)**2 + 4*(layer-1)
## 4*layer**2 - 12*layer + 9 + (4*layer - 4)
## 4*layer**2 - 8*layer + 5
# mod 5: -layer**2 - 3*layer
# if layer == 0 mod 5, then 5 | second corner

# third corner: i == 2
## (2*layer-3)**2 + 6*(layer-1)
## 4*layer**2 - 12*layer + 9 + (6*layer - 6)
## 4*layer**2 - 6*layer + 3
## mod 3: layer**2
## if layer == 0 mod 3, then 3 | third corner 

t0 = time.clock()

MAX = 2**20
#primes = nt.allPrimesLessThan(MAX)
primes = nt.allPrimesLessThan2(MAX)

answer = sum(primes)

def isPrime(n):
    if n < MAX:
        return nt.isPrime(n)
    else:
        return nt.isPrimeNoSieve(n)

i = 2
numPrimeCorners = 0.0
numCorners = 1.0
while True:
    corners = cornerNumsInSpiralSquare(i)[:-1]
    
    if (i % 3 == 2 and i > 2) or i % 7 == 0:
        corners[0] = 1 # drop the 1st corner
    if i % 5 == 0:
        corners[1] = 1 # drop the 2nd corner
    if i % 3 == 0:
        corners[2] = 1 # drop the 3rd corner

    numPrimeCorners += sum([1.0 if n > 1 and isPrime(n) else 0.0 for n in corners])
    numCorners += 4.0
    if i % 1000 == 0:
        print i,numPrimeCorners/numCorners
    if numPrimeCorners/numCorners < 0.1:
        answer = 2*i - 1
        break
    i += 1

print 'answer: {}'.format(answer)
print 'seconds elapsed: {}'.format(time.clock()-t0)
