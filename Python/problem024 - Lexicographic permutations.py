#
# Created by 14chanwa on 2017.03.23
#

# Project Euler - Problem 24
# Lexicographic permutations

# The principle is the following: we shall iterate the permutations in the order until the 1000000th permutation has
# been reached. In order to do so, we remark that the algorithm used to permute the elements is the following:

# 012 -> 021 Switch the 2 last digits
# 021 -> 012 -> 102 Invert the last 2 digits and switch 0 and the second element
# 102 -> 120 Switch the 2 last digits
# 120 -> 102 -> 210 Invert the last 2 digits and switch 0 and the third element
# ...

# 0123 -> 0132 Switch the last 2 digits
# 0132 -> 0123 -> 0213 Invert the last 2 digits and switch 1 and the third element
# 0213 -> 0231 Switch the 2 last digits
# 0231 -> 0213 -> 0312
# 0312 -> 0321
# 0321 -> 0123 -> 1023 Invert the last 3 digits and switch 0 and the second element
# 1023 -> 1032
# 1032 -> 1023 -> 1203
# ...

# We adapt this algorithm to the general case (see function "iterate") and iterate 999999 times.


class Counter:
    def __init__(self):
        self.value = 0


def invert_between_bounds(array, lb, ub):
    """
    Inverts elements of the array between indexes lb and ub (excluded).
    :param array:
    :param lb:
    :param ub:
    :return:
    """
    for i in range(0, (ub - lb) // 2):
        swap(array, lb + i, ub - i - 1)


def swap(array, id1, id2):
    """
    Swaps elements of indexes id1 and id2 in the given array
    :param array:
    :param id1:
    :param id2:
    """
    tmp = array[id1]
    array[id1] = array[id2]
    array[id2] = tmp


def iterate(string, iterations, iterations_counter, current_step=10):
    """
    Iterate the permutation of the string until the number of iterations has been reached
    :param string:
    :param current_step:
    :param iterations:
    :param iterations_counter:
    :return:
    """
    # Handle base case
    if current_step == 1 and iterations_counter.value < iterations and len(string) > 1:
        swap(string, len(string) - 1, len(string) - 2)
        iterations_counter.value += 1
        # print(iterations_counter.value, string)
    else:
        # Perform a sweep without permuting the current number
        if iterations_counter.value < iterations:
            iterate(string, iterations, iterations_counter, current_step - 1)

        # Permute the current number with all the others
        for i in range(0, current_step):
            if iterations_counter.value < iterations:
                # Sort the rest of the array (the algorithm ensures the elements should only be inverted)
                invert_between_bounds(string, len(string) - current_step, len(string))

                # Perform permutation
                swap(string, len(string) - current_step + i, len(string) - current_step - 1)
                iterations_counter.value += 1

                # Iterate below
                iterate(string, iterations, iterations_counter, current_step - 1)


main_string = "0123456789"
main_string = [s for s in main_string]
main_counter = Counter()

# We want the 1000000th combination, so since the beginning we want to iterate 999999 times
iterate(main_string, 999999, main_counter, 10)

print(main_string)
