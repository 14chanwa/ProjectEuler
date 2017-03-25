#
# Created by 14chanwa on 2017.03.23
#

# Project Euler - Problem 23
# Non-abundant sums


def is_abundant(n):
    """
    Determines whether the provided number is abundant or not.
    :param n:
    :return:
    """
    # Get divisors
    divisors = set()
    divisors.add(1)
    for i in range(2, n//2 + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    if sum(divisors) > n:
        return True
    return False


def cannot_be_written_as_sum_of_abundant_numbers(n, abundant_numbers):
    """
    Determines whether the provided number n can be written as a sum of two numbers of abundant_numbers.
    It is preferable that abundant_numbers has an optimized find routine (e.g. hashable frozenset in Python).
    :param n:
    :param abundant_numbers:
    :return:
    """
    for i in abundant_numbers:
        if n - i in abundant_numbers:
            return False
    return True


# Get abundant numbers below 28123
abundant_numbers = set()
for i in range(1, 28124):
    if is_abundant(i):
        abundant_numbers.add(i)
abundant_numbers = frozenset(abundant_numbers)


# Test all numbers below 28123
total_sum = 0
for i in range(1, 28124):
    if cannot_be_written_as_sum_of_abundant_numbers(i, abundant_numbers):
        total_sum += i

print(total_sum)
