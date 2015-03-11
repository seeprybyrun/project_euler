# -*- coding: utf-8 -*-
# The square root of 2 can be written as an infinite continued fraction.
# 
# The infinite continued fraction can be written, √2 = [1;(2)], (2) indicates
# that 2 repeats ad infinitum. In a similar way, √23 = [4;(1,3,1,8)].
# 
# It turns out that the sequence of partial values of continued fractions for
# square roots provide the best rational approximations. Let us consider the
# convergents for √2.
# 
# 1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
# 
# What is most surprising is that the important mathematical constant,
# e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].
# 
# The first ten terms in the sequence of convergents for e are:
# 
# 2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
# 
# The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.
# 
# Find the sum of digits in the numerator of the 100th convergent of the
# continued fraction for e.

import time
import math
import numbertheory as nt
import itertools as it
from fractions import gcd

t0 = time.clock()
answer = -1
convergent = 100

a,b = 0,0

for i in range(convergent,0,-1):
    k = 1
    if i % 3 == 0:
        k = 2*i/3
    elif i == 1:
        k = 2

    if i == convergent:
        a,b = k,1
    else:
        a,b = b,a # invert
        a += k*b # add k
        d = gcd(a,b)
        if d != 1:
            a /= d
            b /= d

print '{}th convergent is {}/{}'.format(convergent,a,b)

answer = sum([int(c) for c in str(a)])

print 'answer: {}'.format(answer)
print 'seconds elapsed: {}'.format(time.clock()-t0)
