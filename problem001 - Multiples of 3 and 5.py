#
# Created by 14chanwa on 2017.02.12
#

# Project Euler - Problem 1
# Multiples of 3 and 5

def problem1(max):

    sum = 0
    
    for i in range(1,max) :
        if (i%3 == 0 or i%5 == 0):
            sum = sum + i

    return sum

print(problem1(1000))