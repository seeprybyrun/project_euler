# -*- coding: utf-8 -*-
# An irrational decimal fraction is created by concatenating the positive
# integers:
# 
# 0.123456789101112131415161718192021...
# 
# It can be seen that the 12th digit of the fractional part is 1.
# 
# If d_n represents the nth digit of the fractional part, find the value of the
# following expression.
# 
# d_1 × d_10 × d_100 × d_1000 × d_10000 × d_100000 × d_1000000

from math import log10
from math import floor
import time

t0 = time.clock()

totDigits = 0
k = 0
maxK = 6
prod = 1
for i in range(1,1000000):
    numDigits = int(floor(log10(i)))+1
    totDigits += numDigits
    if totDigits - numDigits < 10**k and totDigits >= 10**k:
        d = int(str(i)[10**k-totDigits-1])
        prod *= d
        print "d_{0} = {1}".format(10**k,d)
        k += 1
        if k > maxK:
            break
print prod

print "seconds elapsed: {0}".format(time.clock()-t0)
