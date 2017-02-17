#
# Created by 14chanwa on 2017.02.12
#

# Project Euler - Problem 10
# Summation of primes

import tqdm

exec(open("util_primeNumbers.py").read(), globals())

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
            currentPrime = getNthPrime(1, currentPrime + 1)
            
            # Update progress bar
            pbar.update(currentPrime - previousPrime)
            previousPrime = currentPrime

    return sum

print(problem10(2000000))