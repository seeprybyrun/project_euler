import time
import math
import numbertheory as nt

def convergentOfSqrt2(k):
    """Returns (a,b), where a/b is the kth convergent of sqrt(2), and a and b are coprime.
The 1st iteration is 3/2."""
    if memo[k]:
        return memo[k]
    
    if k == 1:
        memo[1] = (3,2)
    else:
        a,b = convergentOfSqrt2(k-1)
        # add one, invert, add one
        a += b
        a,b = b,a
        a += b
        memo[k] = (a,b)

    return memo[k]
    
##    r = [1,2]
##    for i in range(1,k):
##        # add 2
##        r[0] += 2*r[1]
##        # invert
##        r = r[::-1]
##    # add 1 and return
##    r[0] += r[1]
##    return tuple(r)

##print convergentOfSqrt2(1) # 3,2
##print convergentOfSqrt2(2) # 7,5
##print convergentOfSqrt2(3) # 17,12
##print convergentOfSqrt2(4) # 41,29

t0 = time.clock()
answer = 0
MAX = 1000

memo = [None] * (MAX+1)

for k in range(1,MAX+1):
    a,b = convergentOfSqrt2(k)
    if len(str(a)) > len(str(b)):
        answer += 1

print 'answer: {}'.format(answer)
print 'seconds elapsed: {}'.format(time.clock()-t0)
