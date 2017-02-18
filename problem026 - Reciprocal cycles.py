#
# Created by 14chanwa on 2017.02.12
#

# Project Euler - Problem 26
# Reciprocal cycles

def getRecurringCycle(denom):
    """
    Computes the recurring cycle of fraction 1/denom
    returns: list containing the recurring cycle if the fraction has a recurring cycle, else empty list
    """

    recurringCycle = []
    euclideanDivisions = []  
    
    r = 1
  
    while True:
        
        tmp = r*10
        q = tmp // denom
        r = tmp % denom
    
        # If the fraction is finite
        if r == 0:
            return []

        for i in range(0, len(euclideanDivisions)):
            if euclideanDivisions[i] == (q,r):
                return recurringCycle[i:]

        recurringCycle.append(q)
        euclideanDivisions.append((q,r))

def problem26(n):
    """
    Gets the integer q so that 1/q has the longest recurring cycle among fractions 1/d, d >= 1, d < n
    """
    index = 0
    maxCycle = 0
    for i in range(1, n):
        recCy = getRecurringCycle(i)
        if maxCycle < len(recCy):
            print(i, recCy)
            index = i
            maxCycle = max(maxCycle, len(getRecurringCycle(i)))
    return index

#print(getRecurringCycle(97))
#print(len(getRecurringCycle(97)))
print(problem26(1000))
        