#
# Created by 14chanwa on 2017.02.26
#

# Project Euler - Problem 122
# Efficient exponentiation

import math

S = {}
f = {1: 0}
S[1] = set()


def find_minimum_exponentiations(n, S, f):
    if n in f.keys():
        return f[n]

    current_minimum = math.inf
    current_m = {}
    current_sets = {}
    for m in range(n // 2,  0, -1):
        # print("ITER m ", m)
        p = n - m
        tmp = find_minimum_exponentiations(m, S, f) + find_minimum_exponentiations(p, S, f) + 1
        tmp_set = S[m] & S[p]
        if m == p:
            tmp_set.add(m)
            tmp -= find_minimum_exponentiations(m, S, f)
        # print("m", m, " p ", p)
        # print("tmp ", tmp)
        # print("tmp_set ", tmp_set)
        if tmp < current_minimum:
            current_sets.clear()
            current_minimum = tmp
        if tmp <= current_minimum:
            current_m.add(m)
            tmp_set_final = S[current_m] | S[n - current_m]
            tmp_set_final.add(current_m)
            tmp_set_final.add(n - current_m)

    # print("current_m", current_m)

    S[n] = tmp_set_final
    f[n] = current_minimum
    # print("f ", f)
    # print("S ", S)
    return current_minimum

find_minimum_exponentiations(20, S, f)
print(S)
print(f)



# import util_primeNumbers
#
#
# def factorize(n):
#     """
#     Factorizes a NON-PRIME number n under form m * p where m is the largest divisor of n
#     :param n:
#     :return: (m, p) where n = m * p
#     """
#     for i in range(2, n):
#         if n % i == 0:
#             return i, n//i
#
#
# def recursive_multiplication_count(n, history):
#     if n == 1:
#         return 0
#     elif n in history.keys():
#         return history[n]
#     elif util_primeNumbers.is_prime(n):
#         # TODO: compute the optimal way if n is prime ; difficult
#         tmp_res = 1 + recursive_multiplication_count(n-1, history)
#         history[n] = tmp_res
#         return tmp_res
#     else:
#         m, p = factorize(n)
#         return recursive_multiplication_count(m, history) + recursive_multiplication_count(p, history)
#
#
# history = {}
# sum_multiplications = 0
# for k in range(1, 201):
#     sum_multiplications += recursive_multiplication_count(k, history)
# print(history)
# print(sum_multiplications)
