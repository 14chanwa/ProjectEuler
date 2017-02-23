#
# Created by 14chanwa on 2017.02.22
#

# Project Euler - Problem 65
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


# def number_of_digits(n):
#     number = 0
#     while n // 10**number > 0:
#         number += 1
#     return number - 1
#
#
# def string_intersection(s1, s2):
#     out = ""
#     for c in s1:
#         if c in s2 and (not c in out):
#             out += c
#     return out
#
#
# def is_product_pandigital(n, m, p):
#     present_digits = []
#     for s in str(n):
#         present_digits.append(int(s))
#     for s in str(m):
#         present_digits.append(int(s))
#     for s in str(p):
#         present_digits.append(int(s))
#     present_digits.sort()
#     if present_digits == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#         return True
#     return False


# def digit_selection(digit_table):
#     selections = []
#     for digit in digit_table:
#         digit_table_tmp = list(digit_table)
#         digit_table_tmp.remove(digit)
#         selections.append((digit, digit_table_tmp))
#     return selections
#

# def recursive_exploration(digit_table, lhs="", rhs="", state=0, pandigital_results=set()):
#     """
#     Explore all combinations of the 9 digits over the lhs, rhs, result
#     :param digit_table:
#     :param lhs:
#     :param rhs:
#     :param state: 0: lhs selection, 1: rhs selection, 2: result
#     :return:
#     """
#     # print(lhs, rhs)
#     if state == 2:
#         result_string = ""
#         for i in digit_table:
#             result_string += str(i)
#         result_table = [''.join(p) for p in itertools.permutations(result_string)]
#         for result in result_table:
#             if int(lhs) * int(rhs) == int(result):
#                 pandigital_results.add(result)
#     elif state == 0:
#         if len(lhs) < 5:
#             if len(lhs) > 0:
#                 recursive_exploration(digit_table, lhs, rhs, 1, pandigital_results)
#             selections = digit_selection(digit_table)
#             # print(selections)
#             for selection in selections:
#                 recursive_exploration(selection[1], lhs + str(selection[0]), rhs, 0, pandigital_results)
#     elif state == 1:
#         if len(lhs) + len(rhs) < 5:
#             if len(rhs) > 0:
#                 recursive_exploration(digit_table, lhs, rhs, 2, pandigital_results)
#             selections = digit_selection(digit_table)
#             for selection in selections:
#                 recursive_exploration(selection[1], lhs, rhs + str(selection[0]), 1, pandigital_results)
#
#
# # Form all possible products using all digits once
# # Select one digit
#
# # If the left digit counter is < 5 then go to the other term
# # Go to the other term selection BRANCH
# # Select another digit
#
#
# pandigital_results = set()
# digit_table = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# recursive_exploration(digit_table, pandigital_results=pandigital_results)
