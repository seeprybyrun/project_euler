##1             1
##3,5,7,9       3 (+2 each)
##13,17,21,25   5 (+4 each)
##31,37,43,49   7 (+6 each)
# squares of odd integers at each top-right corner!

size = 1001
corner = 1
total = 1
for d in range(2,size,2):
    for i in range(4):
        corner += d
        total += corner
print total
