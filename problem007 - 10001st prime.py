#
# Created by 14chanwa on 2017.02.12
#

# Project Euler - Problem 7
# 10001st prime

from util_primeNumbers import get_nth_prime

def problem7(primeNb):
    return get_nth_prime(primeNb,1)

print(problem7(10001))