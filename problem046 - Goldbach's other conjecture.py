#
# Created by 14chanwa on 2017.02.23
#

# Project Euler - Problem 46
# Goldbach's other conjecture

import util_primeNumbers


def problem046():

    # Store prime numbers
    prime_number_table = [2, 3, 5, 7, 11]

    # Iterate over odd numbers
    multiplier = 1
    while True:
        current_number = 1 + 2 * multiplier
        # Replenish prime table
        while current_number > prime_number_table[-1]:
            prime_number_table.append(util_primeNumbers.get_nth_prime(1, prime_number_table[-1] + 1))
        # Test combination existence over all primes and all squares
        found = False
        for prime in [p for p in prime_number_table if p < current_number + 1]:
            sqroot = 0
            while True:
                if prime + 2 * sqroot**2 == current_number:
                    found = True
                    break
                else:
                    if prime + 2 * sqroot > current_number:
                        break
                    sqroot += 1
            if found:
                break
        else:
            return current_number

        multiplier += 1

print(problem046())
