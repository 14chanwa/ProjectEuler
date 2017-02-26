#
# Created by 14chanwa on 2017.02.26
#

# Project Euler - Problem 122
# Efficient exponentiation

import util_primeNumbers


def factorize(n):
    """
    Factorizes a NON-PRIME number n under form m * p where m is the largest divisor of n
    :param n:
    :return: (m, p) where n = m * p
    """
    for i in range(2, n):
        if n % i == 0:
            return i, n//i


def recursive_multiplication_count(n, history):
    if n == 1:
        return 0
    elif n in history.keys():
        return history[n]
    elif util_primeNumbers.is_prime(n):
        # TODO: compute the optimal way if n is prime ; difficult
        tmp_res = 1 + recursive_multiplication_count(n-1, history)
        history[n] = tmp_res
        return tmp_res
    else:
        m, p = factorize(n)
        return recursive_multiplication_count(m, history) + recursive_multiplication_count(p, history)


history = {}
sum_multiplications = 0
for k in range(1, 201):
    sum_multiplications += recursive_multiplication_count(k, history)
print(history)
print(sum_multiplications)
