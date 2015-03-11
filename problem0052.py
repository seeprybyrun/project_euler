# It can be seen that the number, 125874, and its double, 251748, contain
# exactly the same digits, but in a different order.
# 
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.

import time
import math
import numbertheory as nt

def sameDigits(a,b):
    return sorted(str(a)) == sorted(str(b))

t0 = time.clock()

answer = -1
n = 0

# if ends in 1, then we get last digits = 1,2,3,4,5,6
# if ends in 2, then we get last digits = 2,4,6,8,0,2
# if ends in 3, then we get last digits = 3,6,9,2,5,8
# if ends in 4, then we get last digits = 4,8,2,6,0,4
# if ends in 5, then we get last digits = 5,0,5,0,5,0
# if ends in 6, then we get last digits = 6,2,8,4,0,6
# if ends in 7, then we get last digits = 7,4,1,8,5,2
# if ends in 8, then we get last digits = 8,6,4,2,0,8
# if ends in 9, then we get last digits = 9,8,7,6,5,4
# if ends in 0, then we get last digits = 0,0,0,0,0,0

while True:
    n += 1
    goodNumber = True
    for k in range(2,6+1):
        if not sameDigits(n,k*n):
            goodNumber = False
            break
    if goodNumber:
        answer = n
        #print [k*n for k in range(1,8)]
        break

print 'answer: {0}'.format(answer)
print 'milliseconds elapsed: {0}'.format(1000*(time.clock()-t0))
