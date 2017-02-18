import math

def isPrime(p):
    
    """
    Tests whether the number is prime or not
    """
    if p == 1:
        return False
    if p == 2:
        return True
    if p%2 == 0:
        return False

    for i in range(3, math.floor(math.sqrt(p)) + 1, 2):
        if p%i == 0:
            return False

    return True

def getNthPrime(n, start):

    """
    Gets the nth prime number beginning from start (included)
    """
    counter = 0
    current = start
    
    while True:
        if isPrime(current):
            counter = counter + 1
            if counter >= n:
                return current
        current = current + 1
    
    return current
    