#
# Created by 14chanwa on 2017.02.12
#

# Project Euler - Problem 10
# Summation of primes

import tqdm

from Python.util_primeNumbers import get_nth_prime


def problem10(max):

    """
    Find the sum of all prime numbers inferior to max (included)
    """
    
    if max < 2:
        return 0

    currentPrime = 2
    sum = 0

    # For progress bar
    previousPrime = 2

    with tqdm.tqdm(total=max) as pbar:
        while currentPrime < max:
            sum = sum + currentPrime
            currentPrime = get_nth_prime(1, currentPrime + 1)
            
            # Update progress bar
            pbar.update(currentPrime - previousPrime)
            previousPrime = currentPrime

    return sum

print(problem10(2000000))