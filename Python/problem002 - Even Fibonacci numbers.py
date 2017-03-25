#
# Created by 14chanwa on 2017.02.12
#

# Project Euler - Problem 2
# Even Fibonacci numbers

def problem2(max):
    
    # Iterate over all Fibonacci numbers
    # Sum if even

    if (max < 2): 
        return 0

    sum = 0
    n = 1
    m = 1
    tmp = 0
    
    while True:
        tmp = m
        if tmp > max:
            break

        m = n + m
        n = tmp
        
        if m%2 == 0:
            sum = sum + m

    return sum

print(problem2(4000000))