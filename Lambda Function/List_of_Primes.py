def primes(N):
    I = [2, 3, -1, -5, -6, 7, 8]
    L = list(range(2, N))
    ps = []
    while len(L) > 0:
        p = L[0]
        ps.append(p)
        L = list(filter(lambda x: x % p != 0, L))
    return ps

print(primes(100))
