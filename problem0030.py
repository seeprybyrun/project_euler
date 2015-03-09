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
