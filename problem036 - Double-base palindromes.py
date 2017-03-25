#
# Created by 14chanwa on 2017.03.25
#

# Project Euler - Problem 36
# Double-base palindromes


def convert_integer_to_baseb(n, b):
    """
    Converts a provided integer to a base b > 1. Returns a string corresponding to this number
    :param n:
    :param b:
    :return:
    """
    if n <= 0:
        return "-" + convert_integer_to_baseb(-n, b)

    n_tmp = n
    digits = []
    while n_tmp > 0:
        digits.append(str(n_tmp % b))
        n_tmp //= b

    tmp_str = ''.join(digits)
    return tmp_str[::-1]


# For each number below 1000000, check whether the number written in bases 10 and 2 are palindromes.
total_sum = 0
for i in range(1, 1000000):
    str_b10 = str(i)
    str_b2 = convert_integer_to_baseb(i, 2)
    if str_b10 == str_b10[::-1] and str_b2 == str_b2[::-1]:
        total_sum += i

print(total_sum)
