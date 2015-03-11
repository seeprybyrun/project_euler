# By replacing the 1st digit of the 2-digit number *3, it turns out that six
# of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
# 
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this
# 5-digit number is the first example having seven primes among the ten
# generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
# 56773, and 56993. Consequently 56003, being the first member of this family,
# is the smallest prime with this property.
# 
# Find the smallest prime which, by replacing part of the number (not
# necessarily adjacent digits) with the same digit, is part of an eight prime
# value family.

import time
import math
import numbertheory as nt

t0 = time.clock()

upperBound = 1000000
primes = nt.allPrimesLessThan(upperBound)
answer = -1

for p in primes:
    pStr = str(p)
    numDigits = len(pStr) - 1
    if numDigits < 1:
        continue

    # make a binary string with as many bits as digits
    # the idea is to replace the digits corresponding to 1s
    for i in range(1,2**numDigits):

        # the last bit should always be 0 - replacing the last digit will cause
        # too many nonprimes
        s = bin(i)[2:]
        if len(s) < numDigits:
            s = '0' * (numDigits-len(s)) + s
        s += '0'
        numPrimes = 0
        
        # need to make sure the digits to be replaced are the same
        checkStr = set([pStr[k] for k in range(numDigits) if s[k] == '1'])
        if len(checkStr) > 1:
            continue

        # replace the digits and check for primality
        for j in range(10):
            qStr = ''.join([pStr[k] if s[k] == '0' else str(j) for k in range(numDigits)])
            # also need to make sure the first digit after replacement isn't 0
            if qStr[0] != '0' and nt.isPrime(int(qStr)):
                numPrimes += 1
##            if p == 121313:
##                print qStr,nt.isPrime(int(qStr))
        if numPrimes >= 8:
            answer = p
            break
    if answer > 0:
        break

print 'answer: {0}'.format(answer)
print 'milliseconds elapsed: {0}'.format(1000*(time.clock()-t0))
