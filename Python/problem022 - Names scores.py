#
# Created by 14chanwa on 2017.03.22
#

# Project Euler - Problem 22
# Names scores

# Implements a quicksort algorithm (could have used the build-in sort algorithm in Python).
# String comparison is done by Python (by comparing ASCII numbers of characters).


f = open('p022_names.txt', 'r')

file = f.read()
names = list(map(str, file.split(",")))

# Remove '"'s
for i in range(0, len(names)):
    names[i] = (names[i])[1:len(names[i]) - 1]


def pivot_median_of_three(array, lb, ub):
    """
    Pivot selection method: returns the median elements among the first, last and middle elements of the array
    :param array:
    :param lb: lower bound of the array
    :param ub: upper bound of the array
    :return:
    """
    median_index = (lb + ub) // 2
    if (ub - lb) % 2 == 0:
        median_index -= 1
    if array[lb] < array[median_index] < array[ub - 1] or array[ub - 1] < array[median_index] < array[lb]:
        return median_index
    elif array[lb] < array[ub - 1] < array[median_index] or array[median_index] < array[ub - 1] < array[lb]:
        return ub - 1
    else:
        return lb


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


def quick_sort(array, lb, ub, pivot_method):
    """
    Recursively perform a quick sort on the part [lb, ub] of given array, using the provided pivot selection method.
    :param array:
    :param lb: lower bound of the array
    :param ub: upper bound of the array
    :param pivot_method:
    :return:
    """
    # Initial validity check
    if ub - lb < 2:
        return 0
    else:
        # Choose pivot
        pivot = pivot_method(array, lb, ub)

        # Swap first element
        swap(array, lb, pivot)

        # Rearrange elements
        # i: index position of last element <= pivot
        # j: index of current element
        i = lb
        for j in range(lb, ub):
            if array[j] < array[lb]:
                i += 1
                swap(array, i, j)
        swap(array, i, lb)

        # Count the number of comparisons and recursive calls if necessary
        total_sum = ub - lb - 1
        if i - lb > 1:
            total_sum += quick_sort(array, lb, i, pivot_method)
        if ub - (i + 1) > 1:
            total_sum += quick_sort(array, i + 1, ub, pivot_method)
        return total_sum


def alphabetical_order(c):
    """
    Returns the position of the provided CAPITAL letter in the alphabet, e.g: A -> 1.
    :param c:
    :return:
    """
    # Use ASCII numeration
    return ord(c) - 64


# Sort the names array
quick_sort(names, 0, len(names), pivot_median_of_three)

# Compute name scores
name_scores = []
for i in range(0, len(names)):
    score = 0
    for j in range(0, len(names[i])):
        score += alphabetical_order((names[i])[j])
    score *= i + 1
    name_scores.append(score)


print(sum(name_scores))
