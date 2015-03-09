# The number 3797 has an interesting property. Being prime itself, it
# is possible to continuously remove digits from left to right, and
# remain prime at each stage: 3797, 797, 97, and 7. Similarly we can
# work from right to left: 3797, 379, 37, and 3.
# 
# Find the sum of the only eleven primes that are both truncatable
# from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import numbertheory as nt

def isTruncatable(p):
    if p < 10 or not nt.isPrime(p):
        return False
    pStr = str(p)
    n = len(pStr)
    for i in range(1,n):
        a = int(pStr[:i])
        b = int(pStr[i:])
        #print a,b
        if not nt.isPrime(a) or not nt.isPrime(b):
            return False
    return True

primes = nt.allPrimesLessThan(1000000)

##print isTruncatable(2)
##print isTruncatable(4)
##print isTruncatable(13)
##print isTruncatable(23)
##print isTruncatable(59)
##print isTruncatable(537)
##print isTruncatable(3797)

numTruncatable = 0
tot = 0
for p in primes:
    if isTruncatable(p):
        print p
        numTruncatable += 1
        tot += p
    if numTruncatable == 11:
        break
if numTruncatable != 11:
    print ":("
else:
    print tot

# Observations:
# 1) A truncatable prime's leftmost digit must be 2, 3, 5, or 7 (2,3,-4,-2 mod 9)
# 2) The interior digits of a truncatable prime must be 1, 3, 7, or 9 (1,3,-2,0 mod 9)
# 3) A truncatable prime's rightmost digit must be 3 or 7 (3,-2 mod 9)
#
# If the 

# Truncatable primes:
# 23
# 27 x
# 33 x
# 37
# 53
# 57 x
# 73
# 77 x
# 23~37 = 237
# 53~37 = 537
# 73~37 = 737
# 37~73 = 373
