#Independent Alleles
import math

def prob(k,n):
    p = []
    q = 2**k
    for i in range(n,(q+1)):
        p.append(choose(q,i)* 0.25**i * 0.75**(q-i))
    return sum(p)

def choose(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


print (prob(6,19))