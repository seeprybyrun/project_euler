import time
import math
import numbertheory as nt

def isPalindromic(n):
    return str(n) == str(n)[::-1]

lychrel = {}

def isLychrel(n):
    k = n
    tested = []
    for i in range(50):
        # check memoized list
        if (k in lychrel and not lychrel[k]):
            for j in tested:
                lychrel[j] = False
            return False
        if (k in lychrel and lychrel[k]):
            for j in tested:
                lychrel[j] = True
            return True

        # add the reverse of k to k and check for palindrome
        tested.append(k)
        k += int(str(k)[::-1]) 
        if isPalindromic(k):
            for j in tested:
                lychrel[j] = False
            return False

    # if no palindromes found, all tested (< 10000) are lychrel
    for j in tested:
        if j < 10000:
            lychrel[j] = True
    return True

t0 = time.clock()
answer = 0

for k in range(1,10000):
    if isLychrel(k):
        #print k
        answer += 1

print 'answer: {0}'.format(answer)
print 'milliseconds elapsed: {0}'.format(1000*(time.clock()-t0))
