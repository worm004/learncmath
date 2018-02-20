#import Math
def J(n,q):
    D = 1
    while D <= (q-1)*n:
        D = Math.Ceil(D*q/(q-1))
    return q*n + 1 - D
