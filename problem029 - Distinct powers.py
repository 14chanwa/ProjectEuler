#
# Created by 14chanwa on 2017.03.24
#

# Project Euler - Problem 29
# Distinct powers

# The set data structure ensures each distinct term is only counted once.
distinct_numbers = set()
for a in range(2, 101):
    for b in range(2, 101):
        distinct_numbers.add(a**b)

print(len(distinct_numbers))
