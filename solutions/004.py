
def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome(N):
    largest = 0
    for i in reversed(range(N)):
        for j in reversed(range(N)):
            if is_palindrome(i*j) and i*j > largest:
                largest = i*j
    return largest
            
print(largest_palindrome(999))