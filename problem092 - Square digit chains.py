#
# Created by 14chanwa on 2017.02.18
#

# Project Euler - Problem 92
# Square digit chains

import numpy as np


def transformation(n):
    i = 0
    result = 0
    while n // 10**i != 0:
        result += ((n - (n - n % 10**(i+1))) // 10**i)**2
        i += 1
    return result


def recursive_cycle_count(transformation_function, numbers, starting_index):

    current_index = starting_index
    current_indexes = []
    current_indexes.append(current_index)

    while current_index != 1 and current_index != 89:
        current_index = transformation_function(current_index)
        current_indexes.append(current_index)

    if current_index == 1:
        for index in current_indexes:
            numbers[index] = 1
    elif current_index == 89:
        for index in current_indexes:
            numbers[index] = 89

    print(starting_index, len(current_indexes))

max_number = 10**7
starting_numbers = np.zeros((max_number + 1,), dtype=np.int8)
for i in range(2, max_number + 1):
    if starting_numbers[i] == 0:
        recursive_cycle_count(transformation, starting_numbers, i)

count = 0
for number in starting_numbers:
    if number == 89:
        count += 1

print(count)