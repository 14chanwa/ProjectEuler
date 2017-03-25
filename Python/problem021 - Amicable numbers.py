#
# Created by 14chanwa on 2017.03.22
#

# Project Euler - Problem 21
# Amicable numbers


def find_proper_divisors_sum(n):
    divisors = set()
    divisors.add(1)
    for i in range(2, n//2 + 1):
        if n % i == 0:
            divisors.add(n // i)
            divisors.add(i)
    return divisors

total_sum = 0
explored_numbers = set()
for j in range(1, 10001):
    if j not in explored_numbers:
        sum_1 = sum(find_proper_divisors_sum(j))
        sum_2 = sum(find_proper_divisors_sum(sum_1))
        if sum_2 == j and j != sum_1:
            total_sum += j
            total_sum += sum_1
        explored_numbers.add(j)
        explored_numbers.add(sum_1)

print(total_sum)
