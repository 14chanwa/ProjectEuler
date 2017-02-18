#
# Created by 14chanwa on 2017.02.12
#

# Project Euler - Problem 3
# Largest prime factor

import math

exec(open("util_primeNumbers.py").read(), globals())

def problem3(n):
    
    p = 1

    for i in range(1, math.floor(math.sqrt(n))):
        if n%i == 0:
            if isPrime(i):
                p = i

    return p

print(problem3(600851475143))
#print(isPrime(2))
#print(isPrime(29))
#print(isPrime(27))