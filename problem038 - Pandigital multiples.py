#
# Created by 14chanwa on 2017.02.12
#

# Project Euler - Problem 38
# Pandigital multiples

def getNumberDigits(n):
    """
    Gets the number of digits in n
    """
    d = 0
    while n//(10**d) > 0:
        d = d + 1
    return d

def isPandigital(n):
    """
    Checks if the provided number is pandigital
    """
    strnum = str(n)
    for i in range(1,10):
        count = 0
        for j in range(0,len(strnum)):
            if int(strnum[j]) == i:
                count = count + 1
        if count != 1:
            return False
    return True 

def problem38(nbDigits):
    """
    Gives the largest 1 to 9 nbDigits-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1
    """
    result = 0
    
    # First, if a number has d digits, its multiples will have at least d digits.
    # For the concatenated product to have less than 9 digits, the base integer should then have less than 4 digits.
    # Thus, compute an upper bound for the integer
    imax = 10**(nbDigits // 2)
    
    # A nbDigits number should be inferior to
    nmax = 10**nbDigits

    for i in range(1, imax):
        concatenatedProduct = i
        n = 1
        while getNumberDigits(concatenatedProduct) < nbDigits:
            n = n + 1
            tmp = i * n
            concatenatedProduct = concatenatedProduct * 10**getNumberDigits(tmp) + tmp
        if concatenatedProduct < nmax and result < concatenatedProduct and isPandigital(concatenatedProduct):
            result = concatenatedProduct
            print(i, n, result)

    return result
            
print(problem38(9))