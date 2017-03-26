#
# Created by 14chanwa on 2017.03.26
#

# Project Euler - Problem 45
# Triangular, pentagonal, and hexagonal


def get_nth_triangle_number(n):
    return n * (3 * n - 1) // 2


def get_nth_pentagon_number(n):
    return n * (3 * n - 1) // 2


def get_nth_hexagon_number(n):
    return n * (2 * n - 1)


current_triangle_index = 285
pentagonal_numbers = [get_nth_pentagon_number(1)]
current_pentagon_index = 1
hexagonal_numbers = [get_nth_hexagon_number(1)]
current_hexagon_index = 1

found = False
result = 0

while not found:
    current_triangle_index += 1
    current_triangle_number = get_nth_triangle_number(current_triangle_index)
    while pentagonal_numbers[-1] < current_triangle_number:
        current_pentagon_index += 1
        pentagonal_numbers.append(get_nth_pentagon_number(current_pentagon_index))
    while hexagonal_numbers[-1] < current_triangle_number:
        current_hexagon_index += 1
        hexagonal_numbers.append(get_nth_hexagon_number(current_hexagon_index))
    if current_triangle_number in pentagonal_numbers and current_triangle_number in hexagonal_numbers:
        result = current_triangle_number
        found = True

print(result)
