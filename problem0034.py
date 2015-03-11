# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# 
# Find the sum of all numbers which are equal to the sum of the factorial
# of their digits.
# 
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

# max digits will be 7, since the largest amount a digit can contribute to
# a sum is 9!, and 7*9! has 7 digits, while n*9! has fewer than n digits
# for n > 7. indeed, max possible sum is 7*9! = 2540160

def extract_digits(n):
    return [int(d) for d in str(n)]

factorial_memo = {}
def factorial(n):
    if n < 0 or n % 1 != 0:
        raise ValueError,"n must be a nonnegative integer"
    if n in factorial_memo:
        return factorial_memo[n]
    if n == 0:
        return 1
    else:
        factorial_memo[n] = n*factorial(n-1)
        return factorial_memo[n]

tot = 0
for n in range(10,2540161):
    digits = extract_digits(n)
    if n == sum(map(factorial,digits)):
        print n
        tot += n
print tot
