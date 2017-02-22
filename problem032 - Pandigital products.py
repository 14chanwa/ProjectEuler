#
# Created by 14chanwa on 2017.02.22
#

# Project Euler - Problem 65
# Pandigital products


def number_of_digits(n):
    number = 0
    while n // 10**number > 0:
        number += 1
    return number - 1


def string_intersection(s1, s2):
    out = ""
    for c in s1:
        if c in s2 and (not c in out):
            out += c
    return out


def is_product_pandigital(n, m, p):
    present_digits = []
    for s in str(n):
        present_digits.append(int(s))
    for s in str(m):
        present_digits.append(int(s))
    for s in str(p):
        present_digits.append(int(s))
    present_digits.sort()
    if present_digits == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return True
    return False

pandigital_products = set()

# TODO: form all possible products using all digits once

print(pandigital_products)
sum_products = 0
for product in pandigital_products:
    sum += product
print(sum_products)

