def J3(n):
    N = 3 * n
    while N > n:
        N = int((N - n - 1)/2) + N - n
    return N
