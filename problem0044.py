﻿import time
import math

def isPerfectSquare(x):
    sr = int(math.sqrt(x))
    return x == sr**2

##print isPerfectSquare(0)
##print isPerfectSquare(0.5)
##print isPerfectSquare(1)
##print isPerfectSquare(2)
##print isPerfectSquare(25)
##print isPerfectSquare(25.0)
##print isPerfectSquare(24.99999999)

# m(3m−1) + n(3n−1) == j(3j-1)
# m(3m-1) - n(3n-1) == k(3k-1)
# 3m^2 - m + 3n^2 - n == 3j^2 - j
# 3m^2 - m - 3n^2 + n == 3k^2 - k

# y(3y-1)/2 == x
# 3y^2 - y == 2x
# 3y^2 - y - 2x == 0
# y == (1 \pm \sqrt{1+24x})/6
# if (1 + math.sqrt(1+24*x))/6 is integral, then x is pentagonal
# equivalently, isPerfectSquare(1+24*x) and int(math.sqrt(1+24*x)) % 6 == 5

def isPentagonal(x):
    return isPerfectSquare(1+24*x) and int(math.sqrt(1+24*x)) % 6 == 5

##print isPentagonal(1)
##print isPentagonal(4)
##print isPentagonal(5)
##print isPentagonal(35)
##print isPentagonal(69)
##print isPentagonal(70)

t0 = time.clock()
D = float('inf')

for i in range(1,2200):
    for j in range(1,2200):
        x = i*(3*i-1)/2
        y = j*(3*j-1)/2
        if isPentagonal(x+y) and isPentagonal(abs(x-y)):
            print i,j,abs(x-y)
            D = min(D,abs(x-y))

print 'D = {0}'.format(D)
print 'milliseconds elapsed: {0}'.format(1000*(time.clock()-t0))
