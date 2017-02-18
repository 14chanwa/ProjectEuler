#
# Created by 14chanwa on 2017.02.15
#

# Project Euler - Problem 209
# Circular Logic

def buildBinaryTruthTable(n):
    """
    returns: a list of list of False or True depicting the truth table
    """
    table = []
    for i in range(0, 2**n):
        row = []
        for j in range(0,n):
            if (i // 2**(n - j - 1)) % 2 == 0:
                row.append(False)
            else:
                row.append(True)
        table.append(row)
    return table

def xor(a,b):
    """
    returns: XOR(a,b)
    """
    return not((not a and not b) or (a and b))

import math

def transformation(line):
    tmp = [line[i] for i in range(1, len(line))]
    tmp.append(xor(line[0], line[1] and line[2]))
    return tmp

def getTableRow(index):
    row = []
    for i in range(0, 6):
        if (index // 2**(6 - i - 1) ) % 2 == 0:
            row.append(False)
        else:
            row.append(True)
    return row

def getTableIndex(row):
    index = 0
    for i in range(0, 6):
        if row[i] == True:
            index = index + 2**(6 - i - 1)
    return index

def binomialCoefficient(n, p):
    """
    Returns the number of combinations of p among n elements
    """
    tmp = math.factorial(p) * math.factorial(n-p)
    return math.factorial(n) // tmp


def binaryTruthTable(request, table):
    """
    Given a n-sized request and the 2**n results of the 6dim truth table result formatted, for instance for n = 3, as:
        a b c
        0 0 0
        0 0 1
        0 1 0
        0 1 1
        1 0 0
        1 0 1
        1 1 0
        1 1 1
    returns: the result of the request for the truth table.
    """
    index = 0
    for i in range(0, len(request)):
        if request[i]:
            index = index + 2**(len(request) - i - 1)

    return table[index]

import copy
import time

def recursiveCount(truthTable, currentIndex, start, startTime):
    if start:
        truthTable_1 = copy.copy(truthTable)
        truthTable_1[currentIndex] = True
        truthTable_2 = copy.copy(truthTable)
        truthTable_1[currentIndex] = False
        return recursiveCount(truthTable_1, currentIndex, False, startTime) + recursiveCount(truthTable_2, currentIndex, False, startTime)

    else:
        #print(truthTable)
        previousResult = truthTable[currentIndex]
        nextIndex = getTableIndex(transformation(getTableRow(currentIndex)))
        if truthTable[nextIndex] == None:
            if previousResult == True:
                # then only False
                truthTable_1 = copy.copy(truthTable)
                truthTable_1[nextIndex] = False
                return recursiveCount(truthTable_1, nextIndex, False, startTime)
            else:
                # then True
                truthTable_1 = copy.copy(truthTable)
                truthTable_1[nextIndex] = True
                # or False
                truthTable_2 = copy.copy(truthTable)
                truthTable_2[nextIndex] = False
                return recursiveCount(truthTable_1, nextIndex, False, startTime) + recursiveCount(truthTable_2, nextIndex, False, startTime)
        else:
            # got to an already assigned index
            if not (truthTable[currentIndex] and truthTable[nextIndex]):
                for i in range(0, len(truthTable)):
                    if truthTable[i] == None:
                        return 1 + recursiveCount(truthTable, i, True, startTime)
                #print(time.mktime(time.localtime()) - startTime, " correct branch")
                return 1
            else:
                #print(time.mktime(time.localtime()) - startTime, " incorrect branch")
                return 0        

startTime = time.mktime(time.localtime())
truthTable = [None for i in range(0, 64)]
print(truthTable)
result = recursiveCount(truthTable, 0, True, startTime)
print(result)
print(time.mktime(time.localtime()) - startTime)

#import numpy as np

#def problem209():
#    """
#    Count the possible combinations so that (a, b, c, d, e, f) == (b, c, d, e, f, xor(a, b and c)).
#    Compute the number of possibilities so that t(a, b, c, d, e, f) AND t(b, c, d, e, f, xor(a, b and c)) = True in this case.
#    Add the case when we set "manually" t(a, b, c, d, e, f) = t(b, c, d, e, f, xor(a, b and c)).
#    The desired result is the complimentary: 2**6 - previousCount
#    """

#    table = buildBinaryTruthTable(6)
#    for i in range(0, 2**6):
#        (table[i]).append(xor(table[i][0], table[i][1] and table[i][2]))

#    counts = np.zeros((2**6, ), dtype=np.int32)

#    for i in range(0, 2**6):
#        print(table[i][:6], table[i][1:])
#        if table[i][:6] == table[i][1:]:
#            counts[i] = counts[i] + 1

#    print(counts)
#    print("Il n'y a égalité que pour tous a,..,f True.")

#    print(binomialCoefficient(63, 1))
#    result = 0
#    for i in range(63, 1, -2):
#        result = result + i * 2**(2**6 - 1 - (63 - i) - 2)
#    print(result)
#    result = result // 2 + 2**(2**6 - 1)
#    print(result)
#    print(2**(2**6) - result)
    
#    #print(2**(2**6 - 1)) # + binomialCoefficient(63, 1) * 2**(2**6 - 3))

#problem209()

#def evaluateExpression(request, table):
#    """
#    Given the 6-sized request and the table, returns the value of the expression
#    table(a,b,c,d,e,f) and table(b,c,d,e,f,xor(a,b and c))
#    """
#    return table(a,b,c,d,e,f) and table(b,c,d,e,f,xor(a,b and c))


#import copy

## Brute force solution: will not work
#def recursiveBinaryVectorBuild(combinationList, currentList, remainingIterations, pbar):
#    """
#    Recursively adds all possible (0 or 1)**remainingIterations combinations to the vectorList, starting with vector currentList
#    """
#    if remainingIterations == 0:
#        combinationList.append(currentList)
#        pbar.update(1)
#    else:
#        listCopy = copy.copy(currentList)
#        listCopy.append(False)
#        currentList.append(True)
#        recursiveBinaryVectorBuild(combinationList, listCopy, remainingIterations - 1)
#        recursiveBinaryVectorBuild(combinationList, currentList, remainingIterations - 1)

#import tqdm

## Brute force solution: will not work
#def enumerateBinaryCombinations(n):
#    """
#    returns: a list of all possible combinations of binary variables in a vector of length n
#    """
#    with tqdm.tqdm(total=2**n) as pbar:
#        combinationList = recursiveBinaryVectorBuild([], [], n, pbar)
#    return combinationList

## Brute force solution: will not work
#def problem209():

#    # Enumerate all possible tables
#    print("Enumerating tables...")
#    tablesList = enumerateBinaryCombinations(2**6)
    
#    # Enumerate all possible requests
#    print("Enumerating requests...")
#    requestList = enumerateBinaryCombinations(2**6)    

#    count = 0
#    with tqdm.tqdm(total=len(tablesList)) as pbar:
#        for table in tablesList:
#            for request in requestList:
#                if not evaluateExpression(request, table):
#                    count = count + 1
#            pbar.update(1)

#    return count

#list = []
#recursiveBinaryVectorBuild(list, [], 6)
#print(list)
#print(len(list))

#print(problem209())