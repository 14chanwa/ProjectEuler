#
# Created by 14chanwa on 2017.03.25
#

# Project Euler - Problem 39
# Integer right triangles

# We impose:
# (1) p = a + b + c
# (2) a**2 + b** 2 = c** 2
# (3) 0 < a <= b < c, so with only a and b as variables (c is defined by a, b and (1)), we have:
# (3bis) 0 < a < p / 3 and b < (p-a) / 2

import math

maximum_p = 0
maximum_solutions = 0

for p in range(3, 1001):

    # Count the number of solutions
    solutions_count = 0
    for a in range(1, p // 3):
        for b in range(a, (p - a) // 2):
            if p == a + b + math.sqrt(a ** 2 + b ** 2):
                solutions_count += 1

    # If found new maximum, update
    if solutions_count > maximum_solutions:
        maximum_p = p
        maximum_solutions = solutions_count

print(maximum_p, maximum_solutions)
