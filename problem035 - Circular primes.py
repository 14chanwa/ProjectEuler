#
# Created by 14chanwa on 2017.02.18
#

# Project Euler - Problem 35
# Circular primes

# Get all the prime numbers below 1 million

from util_primeNumbers import is_prime

prime_numbers = []
for i in range(2, 10**6 + 1):
    if is_prime(i):
        prime_numbers.append(i)

print(prime_numbers)
# print(len(prime_numbers))

circular_primes = []

for prime in prime_numbers:
    number_string = str(prime)
    rotations = []
    for i in range(0, len(number_string)):
        number_string = number_string[1:] + number_string[0]
        rotations.append(number_string)
    is_circular = True
    for rotated_prime in rotations:
        if not is_prime(int(rotated_prime)):
            is_circular = False
            break
    if is_circular:
        for rotated_prime in rotations:
            circular_primes.append(int(rotated_prime))

circular_primes = sorted(list(set(circular_primes)))

print(circular_primes)
print(len(circular_primes))
