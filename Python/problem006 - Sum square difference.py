#
# Created by 14chanwa on 2017.02.12
#

# Project Euler - Problem 6
# Sum square difference

def problem6(max):

    """
    Computes the difference between the square of the sum and the sum of the squares of the natural numbers between 1 and max
    """

    sumSquare = 0
    squareSum = 0
    
    for i in range(1, max+1):
        sumSquare = sumSquare + i**2
        squareSum = squareSum + i

    squareSum = squareSum**2

    return abs(sumSquare - squareSum)

print(problem6(100))