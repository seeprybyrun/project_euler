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
