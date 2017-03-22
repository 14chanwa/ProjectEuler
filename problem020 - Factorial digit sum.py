#
# Created by 14chanwa on 2017.03.22
#

# Project Euler - Problem 20
# Factorial digit sum

# It turns out that 100! is still small enough for (64 bits) integers.
# Else, we should have had to implement manually a multiplication algorithm (with an optimized space complexity).


import math


n = math.factorial(100)
n_str = str(n)
result = 0
for i in range(0, len(n_str)):
    result += int(n_str[i])

print(result)
