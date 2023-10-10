def prime_generator():
    primes = []  # List to store prime numbers found so far
    num = 2  # Initial number to check for primality

    while True:
        if all(num % prime != 0 for prime in primes):
            primes.append(num)
            yield num
        num += 1

# Example usage
p = prime_generator()
count = 0
for _ in range(10):
    count += 1
    print(next(p))

for _ in range(10):
    count += 1
    print(next(p))

print(count)
