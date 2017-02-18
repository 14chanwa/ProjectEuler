#
# Created by 14chanwa on 2017.02.12
#

# Project Euler - Problem 3
# Largest prime factor

import math
import util_primeNumbers


def problem3(n):
    
    p = 1

    for i in range(1, math.floor(math.sqrt(n))):
        if n%i == 0:
            if util_primeNumbers.is_prime(i):
                p = i

    return p

print(problem3(600851475143))
#print(isPrime(2))
#print(isPrime(29))
#print(isPrime(27))