import time
import math
import numbertheory as nt

t0 = time.clock()
answer = 0

# Observation 1
# since 100^100 has 201 digits, max number to deal with is
# 9...9 (200 digits), so max sum is 9*200 = 1800

# Observation 2
# digitalSum(x) == x (mod 9)
# so digitalSum(x+9*k) == x (mod 9) for all k

# Observation 3
# if k == floor(b*log10(a)) + 1 is the number of digits, then
# 9*k gives an upper bound on the digital sum

# More observations:
# x == a_0-a_1+a_2-a_3+... (mod 11)
# x == a_0+a_1*10 (mod 100)
# x == a_2*100 + a_1*10 + a_0 (mod 8)
# x == a_1*10 + a_0 (mod 25)

# x mod 8

best = (0,0)

for a in range (2,101):
    for b in range(2,101):
        digitSum = sum([int(c) for c in str(a**b)])
        if digitSum > answer:
            answer = digitSum
            best = a,b

##def digitalSum(a,b):
##    """Computes the sum of the digits in a^b, where 1 <= a,b < 100"""
##
##print digitalSum(10,10)

print 'answer: {},{}'.format(answer,best)
print 'milliseconds elapsed: {0}'.format(1000*(time.clock()-t0))
