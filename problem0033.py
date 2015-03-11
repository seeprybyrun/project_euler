# The fraction 49/98 is a curious fraction, as an inexperienced mathematician
# in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
# which is correct, is obtained by cancelling the 9s.
# 
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# 
# There are exactly four non-trivial examples of this type of fraction, less
# than one in value, and containing two digits in the numerator and
# denominator.
# 
# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.

#(10*a+b)/(10*c+b) == a/c
    # (10*a+b)/a == (10*c+b)/c
    # 10 + b/a == 10 + b/c
    # b/a == b/c
    # a == c
    # so reduced form is 1, so no good
#(10*b+a)/(10*b+c) == a/c
    # (10*b+a)/a == (10*b+c)/c
    # 10*b/a + 1 == 10*b/c + 1
    # b/a == b/c
    # a == c
    # so reduced form is 1, so no good
#(10*a+b)/(10*b+c) == a/c
    # 10 + b/a == 10*b/c + 1
    # 9 == 10*b/c - b/a
    # 9 == b*(10/c - 1/a)
    # b == 9/(10/c - 1/a) == 9*a*c/(10*a - c)
#(10*b+a)/(10*c+b) == a/c
    # 10*b/a + 1 == 10 + b/c
    # 9 == 10*b/a - b/c
    # 9 == b*(10/a - 1/c)
    # b == 9/(10/a - 1/c) == 9*a*c/(10*c - a)

#in all cases, 1 <= a,b,c <= 9
#in all cases, numerator < denominator

for a in range(1,10):
    for c in range(a+1,10): # so reduced form is < 1
        # check that b is integer in [1,9]
        if (9*a*c) % (10*a - c) == 0:
            b = 9*a*c/(10*a - c)
            if 1 <= b <= 9:
                print '{0}{1}/{1}{2} == {0}/{2}'.format(a,b,c)
        if (9*a*c) % (10*c - a) == 0:
            b = 9*a*c/(10*c - a)
            if 1 <= b <= 9:
                print '{1}{0}/{2}{1} == {0}/{2}'.format(a,b,c)
