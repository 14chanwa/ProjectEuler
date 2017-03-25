#
# Created by 14chanwa on 2017.02.12
#

# Project Euler - Problem 4
# Largest palindrome product

import math

def isPalindrome(n):
    
    """
    Checks if n is a palindrome.
    First, get its last digit (its greatest power of 10). Then perform a check taking its digits by pairs.
    """

    pow = 0
    while n // 10**(pow + 1) > 0:
        pow = pow + 1
    
    for k in range(0, math.ceil(pow/2)):
        if (n - n//10**(k + 1) * 10**(k+1)) // 10**k != (n - n//10**(pow-k+1) * 10**(pow-k+1)) //(10**(pow-k)):
            return False
    
    return True

def problem4(nbDigits):
    
    """
    Gets the greatest palindrome formed by the product of two numbers of nbDigits digits
    """
    
    number = 0
    
    for i in range(1, 10**nbDigits):
        for j in range(1, 10**nbDigits):
            n = i * j
            if number < n and isPalindrome(n):
                number = n
    
    return number

print(problem4(3))
#for i in range(1,10000):
#    if isPalindrome(i):
#        print(i)