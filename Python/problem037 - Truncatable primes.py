#
# Created by 14chanwa on 2017.03.25
#

# Project Euler - Problem 37
# Truncatable primes

from Python import util_primeNumbers


def is_truncatable_prime(p):
    p_str = str(p)
    for i in range(len(p_str)):
        if not util_primeNumbers.is_prime(int(p_str[i:])) \
                or not util_primeNumbers.is_prime(int(p_str[:len(p_str) - i])):
            return False
    return True


total_sum = 0
current_prime = 7
truncatable_prime_count = 0
while truncatable_prime_count < 11:
    current_prime = util_primeNumbers.get_nth_prime(1, current_prime + 1)
    if is_truncatable_prime(current_prime):
        total_sum += current_prime
        truncatable_prime_count += 1

print(total_sum)
