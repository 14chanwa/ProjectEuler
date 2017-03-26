#
# Created by 14chanwa on 2017.03.26
#

# Project Euler - Problem 44
# Pentagon numbers


def get_nth_pentagon_number(n):
    return n * (3 * n - 1) // 2


pentagon_numbers = [get_nth_pentagon_number(1)]
max_pentagon_index = 1
current_index = 0

result = 0
found = False

# For each pentagon number, check whether the difference and the sum are pentagon numbers. Could optimize the algorithm
# by using a datastructure such as a set, which guarantees a constant lookup time.
while not found:
    current_pentagon_number = pentagon_numbers[current_index]
    for i in range(1, current_index):
        other_pentagon_number = pentagon_numbers[current_index - i]
        while pentagon_numbers[-1] < current_pentagon_number + other_pentagon_number:
            max_pentagon_index += 1
            pentagon_numbers.append(get_nth_pentagon_number(max_pentagon_index))
        if current_pentagon_number - other_pentagon_number in pentagon_numbers \
                and current_pentagon_number + other_pentagon_number in pentagon_numbers:
            result = current_pentagon_number - other_pentagon_number
            found = True
            break
    current_index += 1
    while current_index + 1 > len(pentagon_numbers):
        max_pentagon_index += 1
        pentagon_numbers.append(get_nth_pentagon_number(max_pentagon_index))

print(result)
