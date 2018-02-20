import math
def J(n,q):
    D = 1
    while D <= (q-1)*n:
        D = math.ceil(D*q/(q-1))
    return q*n + 1 - D
