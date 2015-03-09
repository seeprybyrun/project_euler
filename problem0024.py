import itertools
p = '0123456789'
perms = itertools.permutations(p)
perms = [p for p in perms]
print ''.join(perms[999999])
