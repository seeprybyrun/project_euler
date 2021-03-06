# -*- coding: utf-8 -*-
# Triangle, pentagonal, and hexagonal numbers are generated by the following
# formulae:
# 
# Triangle	 	T_n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	 	P_n=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
# Hexagonal	 	H_n=n(2n−1)	 	1, 6, 15, 28, 45, ...
# It can be verified that T_285 = P_165 = H_143 = 40755.
# 
# Find the next triangle number that is also pentagonal and hexagonal.

import time
import math

def isPerfectSquare(x):
    sr = int(math.sqrt(x))
    return x == sr**2

def isPentagonal(x):
    return isPerfectSquare(1+24*x) and int(math.sqrt(1+24*x)) % 6 == 5

# x = y(2y-1)
# 2y^2 - y - x = 0
# y = (1 + \sqrt{1+8x})/4

##def isHexagonal(x):
##    return isPerfectSquare(1+8*x) and int(math.sqrt(1+8*x)) % 4 == 3

##assert isHexagonal(1)
##assert isHexagonal(6)
##assert isHexagonal(15)
##assert isHexagonal(28)
##assert isHexagonal(45)
##assert not isHexagonal(2)
##assert not isHexagonal(30)
##assert isPentagonal(40755) and isHexagonal(40755)

# rewritten after reviewing Project Euler forums:
# 
# no need to check hexagonality: since hex numbers are
# triangle numbers, just generate the hex numbers and
# check for pentagonality

t0 = time.clock()
index = 143 # H_143 = 40755
next356Num = 0

while not( isPentagonal(next356Num) ):
    index += 1
    next356Num = index*(2*index-1)

print 'next tri/pent/hexagonal number: {0} (hex index = {1})'.format(next356Num,index)
print 'milliseconds elapsed: {0}'.format(1000*(time.clock()-t0))
