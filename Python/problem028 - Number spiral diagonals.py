#
# Created by 14chanwa on 2017.03.24
#

# Project Euler - Problem 28
# Number spiral diagonals


def get_sum_diagonals(spiral_size):
    """
    Gets the sum of the diagonals of a spiral of size spiral_size.
    The size of a spiral is defined as the length of an edge.
    :param spiral_size:
    :return:
    """
    count = 1
    current_number = 1
    for i in range(3, spiral_size + 1, 2):
        for j in range(0, 4):
            current_number += i - 1
            count += current_number
            # print(current_number, count)
    return count


print(get_sum_diagonals(1001))
