#
# Created by 14chanwa on 2017.03.25
#

# Project Euler - Problem 41
# Pandigital prime

# This is a suboptimal solution (test all primes below 10**9, check whether all proper digits appear once).
# A perhaps better algorithm would be: list all pandigital numbers (there are only 409113 such numbers) and check the
# primality of each of them from the greatest to the lowest.

from itertools import permutations
import util_primeNumbers


def get_maximum_pandigital_prime():
    base_sequence = "987654321"
    for i in range(0, 9):
        sequence = base_sequence[i:]
        perm = [int(''.join(p)) for p in permutations(sequence)]
        perm.sort(reverse=True)
        for p in perm:
            if util_primeNumbers.is_prime(p):
                return p

print(get_maximum_pandigital_prime())
