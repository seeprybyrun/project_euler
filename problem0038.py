# -*- coding: utf-8 -*-
# Take the number 192 and multiply it by each of 1, 2, and 3:
# 
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# 
# By concatenating each product we get the 1 to 9 pandigital, 192384576.
# We will call 192384576 the concatenated product of 192 and (1,2,3)
# 
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
# and 5, giving the pandigital, 918273645, which is the concatenated product
# of 9 and (1,2,3,4,5).
# 
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as
# the concatenated product of an integer with (1,2, ... , n) where n > 1?

import time

def concatProd(n,k):
    return int(''.join([str(n*(i+1)) for i in range(k)]))

def isPandigital(n,k):
    return sorted([c for c in str(n)]) == [str(i+1) for i in range(k)]
    
##print concatProd(192,3) # 192384576
##print concatProd(9,5) # 918273645
##print isPandigital(123456789,9) # true
##print isPandigital(987123645,9) # true
##print isPandigital(111111111,9) # false
##print isPandigital(12,2) # true
##print isPandigital(12,3) # false

# need n to start with 9
# roughly need something like log10(n) ~ 9/k
# need to beat 918273645

t0 = time.clock()

maxPandigital = concatProd(9,5)

for i in range(9182,10000):
    if '0' in str(i): continue
    n = concatProd(i,2)
    if isPandigital(n,9) and n > maxPandigital:
        maxPandigital = n

print "biggest 1-9 pandigital: {0}".format(maxPandigital)
print "seconds elapsed: {0}".format(time.clock()-t0)
