#
# Created by 14chanwa on 2017.02.12
#

# Project Euler - Problem 5
# Smallest multiple


from Python.util_primeNumbers import is_prime


def problem5(maxEven):

    """
    Finds the smallest positive number to be evenly divisible by all numbers from 1 to maxEven (included).
    Determine the most restrictive prime number combination necessary for the number to be divisible by all the mentionned integers.
    The smallest number will then be the product of these prime numbers.
    """

    # Look for prime powers
    primePowers = {}
    
    for i in range(maxEven, 1, -1):
        currentPrimePowers = {}
        currentProduct = i
        while currentProduct > 1:
            for j in range(currentProduct, 1, -1):
                if currentProduct%j == 0 and is_prime(j):
                    
                    if currentPrimePowers.__contains__(j):
                        currentPrimePowers[j] = currentPrimePowers[j] + 1
                    else:
                        currentPrimePowers[j] = 1
                    
                    currentProduct = currentProduct // j
                    continue
        
        for key in currentPrimePowers.keys():
            if primePowers.__contains__(key):
                primePowers[key] = max(primePowers[key], currentPrimePowers[key])
            else:
                primePowers[key] = currentPrimePowers[key]
    
    # Form smallest product
    result = 1
    for key, value in primePowers.items():
        result = result * key**value
    
    
    return result

print(problem5(20))

# Brute force solution ; computation time is horrible
#def problem5_1(maxEven):

#    """
#    Finds the smallest positive number to be evenly divisible by all numbers from 1 to maxEven (included).
#    """
    
#    # The number is necessarily greater than maxEven (and smaller than factor(maxEven))
#    current = maxEven
#    found = False

#    while not found:
#        found = True
#        for i in range(maxEven, 1, -1):
#            if current%i > 0:
#                current = current + 1
#                found = False
#                continue
        
#    return current