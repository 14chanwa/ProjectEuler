#
# Created by 14chanwa on 2017.02.15
#

# Project Euler - Problem 209
# Circular Logic

# With courtesy of 14vigne


# We consider the transformation (a, b, c, d, e, f) -> (b, c, d, e, f, a xor (b and c)).
# As we can demonstrate that if (b1, c1, d1, e1, f1, a1 xor (b1 and c1) = (b2, c2, d2, e2, f2 a2 xor (b2 and c2) implies
# a1 = a2, ..., f1 = f2 then the transformation partitions the space in cycles. First, we  compute the different cycles
# and their lengths.
# Using the condition:
# T(a, b, c, d, e, f) and T(b, c, d, e, f, a xor (b and c)) == 0    (C)
# we compute the number of "degrees of freedom" of T per cycle of length N. Summing all these degrees over the cycle
# composing the partition of the entire space, we deduce the degrees of freedom of the T verifying (C) over all possible
# values of (a, b, c, d, e, f).

import numpy as np


def xor(a,b):
    """
    Returns a XOR b
    :param a: boolean
    :param b: boolean
    :return: boolean
    """
    return not((not a and not b) or (a and b))


def transformation(line):
    """
    Given 6 booleans, returns the line transformed by: (a, b, c, d, e, f) -> (b, c, d, e, f, a xor (b and c))
    :param line: a list of 6 booleans
    :return: a list of 6 booleans
    """
    tmp = [line[i] for i in range(1, len(line))]
    tmp.append(xor(line[0], line[1] and line[2]))
    return tmp


def get_table_row(index):
    """
    Given the index of the row in a cannonically ordered truth table, returns corresponding the list of 6 booleans.
    :param index: index of the row in an ordered truth table
    :return: a list of 6 booleans
    """
    row = []
    for i in range(0, 6):
        if (index // 2**(6 - i - 1) ) % 2 == 0:
            row.append(False)
        else:
            row.append(True)
    return row


def get_table_index(row):
    """
    Given a list of 6 booleans, returns the corresponding row index in a cannonically ordered truth table.
    :param row: a list of 6 booleans
    :return: integer
    """
    index = 0
    for i in range(0, 6):
        if row[i]:
            index += 2**(6 - i - 1)
    return index


def recursive_cycle_count(cycle_counts, transformation_function, truth_table, current_index=0, current_count=0, start=True):
    """
    Given the transformation function (must be injective), stores in the dictionnary cycle_counts the number of circles
    of length N partitionning space.
    :param cycle_counts:
    :param transformation_function: a function mapping 6 booleans to 6 booleans
    :param truth_table:
    :param current_index:
    :param current_count
    :param start:
    :return:
    """
    if start:
        for i in range(len(truth_table)):
            if truth_table[i] == 0:
                recursive_cycle_count(cycle_counts, transformation_function, truth_table, i, start=False)
                break
    else:
        if truth_table[current_index] == 1:
            if current_count in cycle_counts.keys():
                cycle_counts[current_count] += 1
            else:
                cycle_counts[current_count] = 1
            recursive_cycle_count(cycle_counts, transformation_function, truth_table)
        else:
            next_index = get_table_index(transformation_function(get_table_row(current_index)))
            truth_table[current_index] = 1
            recursive_cycle_count(cycle_counts, transformation_function, truth_table, next_index, current_count + 1,
                                  start=False)


cycle_counts = {}
truth_table = np.zeros((2**6,), dtype=np.int32)
recursive_cycle_count(cycle_counts, transformation, truth_table)

print("Found cycles: ", cycle_counts)

# u0 = undefined
# u1 = 1
# u2 = 3
# u3 = 4
u = [0, 1, 3, 4]
# v0 = 1
# v1 = 2
# v2 = 3
v = [1, 2, 3]

# Compute the max of u indexes
max_u = max(list(cycle_counts.keys()))

# Compute v
for i in range(3, max_u):
    v.append(v[i-2] + v[i-1])

# Compute u
for i in range(4, max_u + 1):
    u.append(v[i-3] + v[i-1])

# Compute the result
result = 1
for key in cycle_counts.keys():
    result *= (u[key])**cycle_counts[key]

print(result)

# def buildBinaryTruthTable(n):
#     """
#     returns: a list of list of False or True depicting the truth table
#     """
#     table = []
#     for i in range(0, 2**n):
#         row = []
#         for j in range(0,n):
#             if (i // 2**(n - j - 1)) % 2 == 0:
#                 row.append(False)
#             else:
#                 row.append(True)
#         table.append(row)
#     return table
#
# def xor(a,b):
#     """
#     returns: XOR(a,b)
#     """
#     return not((not a and not b) or (a and b))
#
# import math
#
#
# def transformation(line):
#     tmp = [line[i] for i in range(1, len(line))]
#     tmp.append(xor(line[0], line[1] and line[2]))
#     return tmp
#
#
# def getTableRow(index):
#     row = []
#     for i in range(0, 6):
#         if (index // 2**(6 - i - 1) ) % 2 == 0:
#             row.append(False)
#         else:
#             row.append(True)
#     return row
#
# def getTableIndex(row):
#     index = 0
#     for i in range(0, 6):
#         if row[i] == True:
#             index = index + 2**(6 - i - 1)
#     return index
#
# def binomialCoefficient(n, p):
#     """
#     Returns the number of combinations of p among n elements
#     """
#     tmp = math.factorial(p) * math.factorial(n-p)
#     return math.factorial(n) // tmp
#
#
# def binaryTruthTable(request, table):
#     """
#     Given a n-sized request and the 2**n results of the 6dim truth table result formatted, for instance for n = 3, as:
#         a b c
#         0 0 0
#         0 0 1
#         0 1 0
#         0 1 1
#         1 0 0
#         1 0 1
#         1 1 0
#         1 1 1
#     returns: the result of the request for the truth table.
#     """
#     index = 0
#     for i in range(0, len(request)):
#         if request[i]:
#             index = index + 2**(len(request) - i - 1)
#
#     return table[index]
#
# import copy
# import time
#
# def recursiveCount(truthTable, currentIndex, start, startTime):
#     if start:
#         truthTable_1 = copy.copy(truthTable)
#         truthTable_1[currentIndex] = True
#         truthTable_2 = copy.copy(truthTable)
#         truthTable_1[currentIndex] = False
#         return recursiveCount(truthTable_1, currentIndex, False, startTime) + recursiveCount(truthTable_2, currentIndex, False, startTime)
#
#     else:
#         #print(truthTable)
#         previousResult = truthTable[currentIndex]
#         nextIndex = getTableIndex(transformation(getTableRow(currentIndex)))
#         if truthTable[nextIndex] == None:
#             if previousResult == True:
#                 # then only False
#                 truthTable_1 = copy.copy(truthTable)
#                 truthTable_1[nextIndex] = False
#                 return recursiveCount(truthTable_1, nextIndex, False, startTime)
#             else:
#                 # then True
#                 truthTable_1 = copy.copy(truthTable)
#                 truthTable_1[nextIndex] = True
#                 # or False
#                 truthTable_2 = copy.copy(truthTable)
#                 truthTable_2[nextIndex] = False
#                 return recursiveCount(truthTable_1, nextIndex, False, startTime) + recursiveCount(truthTable_2, nextIndex, False, startTime)
#         else:
#             # got to an already assigned index
#             if not (truthTable[currentIndex] and truthTable[nextIndex]):
#                 for i in range(0, len(truthTable)):
#                     if truthTable[i] == None:
#                         return 1 + recursiveCount(truthTable, i, True, startTime)
#                 #print(time.mktime(time.localtime()) - startTime, " correct branch")
#                 return 1
#             else:
#                 #print(time.mktime(time.localtime()) - startTime, " incorrect branch")
#                 return 0
#
# startTime = time.mktime(time.localtime())
# truthTable = [None for i in range(0, 64)]
# print(truthTable)
# result = recursiveCount(truthTable, 0, True, startTime)
# print(result)
# print(time.mktime(time.localtime()) - startTime)
#
# #import numpy as np
#
# #def problem209():
# #    """
# #    Count the possible combinations so that (a, b, c, d, e, f) == (b, c, d, e, f, xor(a, b and c)).
# #    Compute the number of possibilities so that t(a, b, c, d, e, f) AND t(b, c, d, e, f, xor(a, b and c)) = True in this case.
# #    Add the case when we set "manually" t(a, b, c, d, e, f) = t(b, c, d, e, f, xor(a, b and c)).
# #    The desired result is the complimentary: 2**6 - previousCount
# #    """
#
# #    table = buildBinaryTruthTable(6)
# #    for i in range(0, 2**6):
# #        (table[i]).append(xor(table[i][0], table[i][1] and table[i][2]))
#
# #    counts = np.zeros((2**6, ), dtype=np.int32)
#
# #    for i in range(0, 2**6):
# #        print(table[i][:6], table[i][1:])
# #        if table[i][:6] == table[i][1:]:
# #            counts[i] = counts[i] + 1
#
# #    print(counts)
# #    print("Il n'y a égalité que pour tous a,..,f True.")
#
# #    print(binomialCoefficient(63, 1))
# #    result = 0
# #    for i in range(63, 1, -2):
# #        result = result + i * 2**(2**6 - 1 - (63 - i) - 2)
# #    print(result)
# #    result = result // 2 + 2**(2**6 - 1)
# #    print(result)
# #    print(2**(2**6) - result)
#
# #    #print(2**(2**6 - 1)) # + binomialCoefficient(63, 1) * 2**(2**6 - 3))
#
# #problem209()
#
# #def evaluateExpression(request, table):
# #    """
# #    Given the 6-sized request and the table, returns the value of the expression
# #    table(a,b,c,d,e,f) and table(b,c,d,e,f,xor(a,b and c))
# #    """
# #    return table(a,b,c,d,e,f) and table(b,c,d,e,f,xor(a,b and c))
#
#
# #import copy
#
# ## Brute force solution: will not work
# #def recursiveBinaryVectorBuild(combinationList, currentList, remainingIterations, pbar):
# #    """
# #    Recursively adds all possible (0 or 1)**remainingIterations combinations to the vectorList, starting with vector currentList
# #    """
# #    if remainingIterations == 0:
# #        combinationList.append(currentList)
# #        pbar.update(1)
# #    else:
# #        listCopy = copy.copy(currentList)
# #        listCopy.append(False)
# #        currentList.append(True)
# #        recursiveBinaryVectorBuild(combinationList, listCopy, remainingIterations - 1)
# #        recursiveBinaryVectorBuild(combinationList, currentList, remainingIterations - 1)
#
# #import tqdm
#
# ## Brute force solution: will not work
# #def enumerateBinaryCombinations(n):
# #    """
# #    returns: a list of all possible combinations of binary variables in a vector of length n
# #    """
# #    with tqdm.tqdm(total=2**n) as pbar:
# #        combinationList = recursiveBinaryVectorBuild([], [], n, pbar)
# #    return combinationList
#
# ## Brute force solution: will not work
# #def problem209():
#
# #    # Enumerate all possible tables
# #    print("Enumerating tables...")
# #    tablesList = enumerateBinaryCombinations(2**6)
#
# #    # Enumerate all possible requests
# #    print("Enumerating requests...")
# #    requestList = enumerateBinaryCombinations(2**6)
#
# #    count = 0
# #    with tqdm.tqdm(total=len(tablesList)) as pbar:
# #        for table in tablesList:
# #            for request in requestList:
# #                if not evaluateExpression(request, table):
# #                    count = count + 1
# #            pbar.update(1)
#
# #    return count
#
# #list = []
# #recursiveBinaryVectorBuild(list, [], 6)
# #print(list)
# #print(len(list))
#
# #print(problem209())