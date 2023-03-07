# Quick test. Find prime numbers in a list from 2 to 100

# Slow solution. 2x for loops
prime_numbers = []
for i in range(2, 101):
    is_prime = True
    for x in range(2, i):
        if i % x == 0:
            is_prime = False
            break
    if is_prime: prime_numbers.append(i)
print(prime_numbers)