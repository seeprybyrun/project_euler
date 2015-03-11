# Surprisingly there are only three numbers that can be written as the sum
# of fourth powers of their digits:
# 
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# 
# Find the sum of all the numbers that can be written as the sum of
# fifth powers of their digits.

POWER = 5
MAX = (POWER+1) * (9**POWER)

tot = 0
for a in range(2,MAX):
    digits = [a/10**i % 10 for i in range(POWER+1)]
    sum_of_digits_power = sum([d**POWER for d in digits])
    if a == sum_of_digits_power:
        to_print = "{0} = ".format(a)
        for d in digits:
            to_print += "{0}^{1} + ".format(d,POWER)
        print to_print
        tot += a
print tot
