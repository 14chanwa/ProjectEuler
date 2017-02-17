#
# Created by 14chanwa on 2017.02.12
#

# Project Euler - Problem 9
# Special Pythagorean triplet

def problem9():
    
    a = 0
    b = 0
    c = 999
    
    # Loop over the decreasing value of c
    # Since a,b,c >=0, a < b < c and a + b + c = 1000 then c <= 999
    while c > -1:
        
        # Since b > a, b should be strictly greater than (1000-c)//2
        for b in range((1000 - c)//2 + 1, 1000 - c):
            
            # Since a + b + c = 1000
            a = 1000 - b - c      

            if a + b + c == 1000 and a**2 + b**2 == c**2:
                return a*b*c
            
        c = c - 1

print(problem9())