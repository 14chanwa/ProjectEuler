#
# Created by 14chanwa on 2017.02.12
#

# Project Euler - Problem 12
# Highly divisible triangular number

import math

def countDivisors(n):
    """
    Counts the number of divisors of n
    """
    count = 0    

    for i in range(1, math.floor(math.sqrt(n))):
        if n%i == 0:
            count = count + 2
    
    if n%math.floor(math.sqrt(n)) == 0:
        count = count + 1
    return count 

def problem12(nbDivisors):
    """
    Returns the first triangle number to have over nbDivisors divisors
    """
    n = 1

    while True:
        currentNumber = (n * (n + 1)) // 2
        if countDivisors(currentNumber) > nbDivisors - 1:
            return currentNumber
        n = n + 1

print(problem12(500))