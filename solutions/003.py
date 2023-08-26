def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def find_largest_prime_factor(n):
    largest_prime = 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print(i, n//i)
            if is_prime(n//i):
                return n//i
            if is_prime(i):
                largest_prime = i
    return largest_prime

print(find_largest_prime_factor(600851475143))
