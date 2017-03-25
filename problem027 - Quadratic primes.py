#
# Created by 14chanwa on 2017.03.24
#

# Project Euler - Problem 27
# Quadratic primes

import util_primeNumbers


def get_maximum_consecutive_primes(a, b):
    count = 0
    n = 0
    while True:
        p = n ** 2 + a * n + b
        if p > 0 and util_primeNumbers.is_prime(p):
            count += 1
            n += 1
        else:
            break
    return count


max_count = 0
max_product = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        current_count = get_maximum_consecutive_primes(a, b)
        if current_count > max_count:
            max_count = current_count
            max_product = a * b

print(max_count, max_product)
