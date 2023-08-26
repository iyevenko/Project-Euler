def fib(N):
    a, b = 1, 2
    while a < N:
        if a % 2 == 0: 
            yield a
        a, b = b, a + b

print(sum(fib(4e6)))