def f(a, b, N):
    na = (N - 1) // a
    nb = (N - 1) // b
    nab = (N - 1) // (a * b)
    return a * na * (na+1) // 2 + \
           b * nb * (nb+1) // 2 - \
           a * b * nab * (nab + 1) // 2

print(f(3, 5, 1000))