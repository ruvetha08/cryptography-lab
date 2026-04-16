import random

def is_prime(n, k=5):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0: return False

    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
            
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
            
    return True

num = int(input("Enter a number to test: "))
iterations = int(input("Enter number of iterations (e.g., 5): "))

if is_prime(num, iterations):
    print(f"{num} is probably prime.")
else:
    print(f"{num} is composite.")
