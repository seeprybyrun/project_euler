def isPalindrome(s):
    n = len(s)
    for i in range(n):
        if s[i] != s[n-i-1]:
            return False
    return True

def decToBin(n):
    if n == 0: return 0
    out = 0
    digit = 0
    while n > 0:
        if n % 2 == 1:
            out += 10**digit
        digit += 1
        n /= 2
    return out

def binToDec(n):
    if n == 0: return 0
    out = 0
    digit = 0
    while n > 0:
        if n % 10 == 1:
            out += 2**digit
        digit += 1
        n /= 10
    return out

assert isPalindrome('101')
assert isPalindrome('110011')
assert not isPalindrome('1010')

assert decToBin(1) == 1
assert decToBin(10) == 1010
assert decToBin(2) == 10
assert decToBin(0) == 0
assert decToBin(9) == 1001

assert binToDec(0) == 0
assert binToDec(1) == 1
assert binToDec(1010) == 10
assert binToDec(10) == 2
assert binToDec(1001) == 9

tot = 0
for i in range(1000000):
    if isPalindrome(str(i)) and isPalindrome(str(decToBin(i))):
        print i,decToBin(i)
        tot += i
print "sum:", tot
