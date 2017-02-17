#
# Created by 14chanwa on 2017.02.12
#

# Project Euler - Problem 7
# 10001st prime

exec(open("util_primeNumbers.py").read(), globals())

def problem7(primeNb):
    return getNthPrime(primeNb,1)

print(problem7(10001))