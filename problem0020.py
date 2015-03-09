from ent import *

def proper_divisors(n):
    pf = factor(n)
    sigma_0 = exp(sum([log(e) for p,e in pf]))
    for i in range(sigma_0 - 1):
        

def totient(n):
    phi = 1
    for p,e in factor(n):
        phi *= p**(e-1) * (p-1)
    return phi

N = 10000

for i in range(N):
    
