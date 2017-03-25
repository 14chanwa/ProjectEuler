#
# Created by 14chanwa on 2017.03.25
#

# Project Euler - Problem 34
# Digit factorials

import math

# An upper bound for the problem is the condition: if n is the number of digits, then n * 9! > 10**n.
# Let n_max be the last n for which this condition holds:
n_max = 0
while (n_max + 1) * math.factorial(9) > 10**(n_max + 1):
    n_max += 1

total_sum = 0

# 1! and 2! are not included
for number in range(3, 10**n_max):
    str_number = str(number)
    left_member = 0
    for d in str_number:
        left_member += math.factorial(int(d))
    if left_member == number:
        total_sum += number

print(total_sum)
