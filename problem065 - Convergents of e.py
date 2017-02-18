#
# Created by 14chanwa on 2017.02.18
#

# Project Euler - Problem 65
# Convergents of e

import fractions


def compute_e_continuous_fraction(n):
    """
    Computes the continuous fraction of e up to order n
    :param n:
    :return:
    """
    continuous_fraction = [2]
    k = 1
    while len(continuous_fraction) < n:
        continuous_fraction.append(1)
        continuous_fraction.append(2 * k)
        continuous_fraction.append(1)
        k += 1
    return continuous_fraction


def compute_nth_convergent(continuous_fraction, n):
    """
    Computes the nth convergent associated to the provided continuous fraction
    :param continuous_fraction:
    :param n:
    :return:
    """

    if n > len(continuous_fraction):
        return 0

    convergent = fractions.Fraction(continuous_fraction[n-1], 1)

    for i in range(n - 2, -1, -1):
        convergent = continuous_fraction[i] + fractions.Fraction(1, convergent)

    return convergent


continuous_fraction = compute_e_continuous_fraction(1000)
print(continuous_fraction)

convergent = compute_nth_convergent(continuous_fraction, 100)
print(convergent)

# Sum of the digits of the numerator
numerator = str(convergent.numerator)
digit_sum = 0
for i in numerator:
    digit_sum += int(i)
print(digit_sum)
