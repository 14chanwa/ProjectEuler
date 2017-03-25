#
# Created by 14chanwa on 2017.02.18
#

# Project Euler - Problem 014
# Longest Collatz sequence

import numpy as np


def iterate_sequence(n):
    if n % 2 == 0:
        return n//2
    else:
        return 3*n + 1


def recursively_iterate(table, current_number, length=0, maximum_index=10**6):
    """
    For the given table, iterates over a cycle
    :param table: the table of available starting numbers (if a number was already crossed, every cycle starting at this
    number will be shorter that one of those already explored.
    :param current_number:
    :param length: the length of the current cycle
    :return:
    """
    # Mark the number as crossed by
    if current_number < maximum_index + 1:
        table[current_number] = 1

    if current_number == 1:
        return length + 1
    else:
        return recursively_iterate(table, iterate_sequence(current_number), length + 1)


# The index 0 is useless
maximum_index = 10**6
table = np.zeros((maximum_index + 1,), dtype=np.bool_)
max_length = 0
max_length_index = 0
for i in range(1, maximum_index + 1):
    if table[i] == 0:
        tmp = recursively_iterate(table, i)
        if tmp > max_length:
            max_length_index = i
            max_length = tmp

print(max_length_index, max_length)
