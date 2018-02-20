#import Math
def J3(n):
    D = 1
    while D <= 2*n:
        D = Math.Ceil(D*3/2)
    return 3*n + 1 - D
