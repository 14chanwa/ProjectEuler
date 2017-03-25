#
# Created by 14chanwa on 2017.02.22
#

# Project Euler - Problem 32
# Pandigital products

import itertools

# List all permutations of 1..9
permutation_list = [''.join(p) for p in itertools.permutations("123456789")]
print(len(permutation_list), " permutations found")
pandigital_results = set()

# Select the n first digits as the lhs, the m following digits as the rhs, the rest as the result
# Check if pandigital
for lhs_digits in range(1, 6):
    for rhs_digits in range(1, 6 - lhs_digits):
        for permutation in permutation_list:
            lhs = int(permutation[:lhs_digits])
            rhs = int(permutation[lhs_digits:lhs_digits+rhs_digits])
            res = int(permutation[lhs_digits+rhs_digits:])
            if lhs * rhs == res:
                pandigital_results.add(res)


print(pandigital_results)
sum_products = 0
for product in pandigital_results:
    sum_products += product
print(sum_products)
