#
# Created by 14chanwa on 2017.02.14
#

# Project Euler - Problem 202
# Laserbeam

# Let us represent the mirrors as a pyramid :
#   /\
#  /\/\
# /\/\/\
# ......
# The beam starts at the vertex at the top. When the beam is reflected, it is equivalent to say that it goes through an edge from top to bottom.
# If the beam does not cross any vertex from the top to the next to last row but exits at the last row, then it crosses one edge for the first row of triangles, and two edges for each other row to the next  to last row. Then, the number of reflections is necessarily odd and equals to (number of rows - 2) * 2 + 1.
# Let us take all the vertexes in the last row. The answer to the question is the number of "C" vertexes in this row that do not belong to a trajectory crossing one or many vertexes inside the pyramid.
# If the row 0 consists in a sigle "C", then the "C"s in row number n are located at indexes (starting 0) 3*k + (3-n)%3 between 0 and n
# Let us consider a pyramid composed of N rows and a beam that crosses one or many vertex before the Nth row. Let M be the first row number for which the beam crosses one vertex. For a matter of symmetry, if it crosses the last row, then M divides N. Moreover, if the first crossed vertex is in position V (starting 0) in the row M, then the position of the associated crossed vertex in the row N is indexed V * N / M. This means that if a divisor of N (except 1) divides the index, it should be removed.

def buildPyramid(reflectionNumber):
    """
    Visualize the problem
    For small reflectionNumber only
    """

    rowCount = (reflectionNumber - 1) // 2 + 2
    # rowCount should be > 1
    if rowCount < 2:
        return 0

    # A = 0
    # B = 1
    # C = 2
    # Building the pyramid
    pyramid = [[2], [0, 1]]
    for i in range(2, rowCount):
        row = []
        for j in range(1, i):
            if ((pyramid[i-1])[j-1] == 0 and (pyramid[i-1])[j] == 1) or ((pyramid[i-1])[j-1] == 1 and (pyramid[i-1])[j] == 0):
                row.append(2)
            elif ((pyramid[i-1])[j-1] == 1 and (pyramid[i-1])[j] == 2) or ((pyramid[i-1])[j-1] == 2 and (pyramid[i-1])[j] == 1):
                row.append(0)
            elif ((pyramid[i-1])[j-1] == 0 and (pyramid[i-1])[j] == 2) or ((pyramid[i-1])[j-1] == 2 and (pyramid[i-1])[j] == 0):
                row.append(1)
        
        # First element
        if ((pyramid[i-1])[0] == 0 and row[0] == 1) or ((pyramid[i-1])[0] == 1 and row[0] == 0):
            row.insert(0, 2)
        elif ((pyramid[i-1])[0] == 1 and row[0] == 2) or ((pyramid[i-1])[0] == 2 and row[0] == 1):
            row.insert(0, 0)
        elif ((pyramid[i-1])[0] == 0 and row[0] == 2) or ((pyramid[i-1])[0] == 2 and row[0] == 0):
            row.insert(0, 1)
        
        # Last element
        if ((pyramid[i-1])[i-1] == 0 and row[i-1] == 1) or ((pyramid[i-1])[i-1] == 1 and row[i-1] == 0):
            row.append(2)
        elif ((pyramid[i-1])[i-1] == 1 and row[i-1] == 2) or ((pyramid[i-1])[i-1] == 2 and row[0] == 1):
            row.append(0)
        elif ((pyramid[i-1])[i-1] == 0 and row[i-1] == 2) or ((pyramid[i-1])[i-1] == 2 and row[i-1] == 0):
            row.append(1)

        pyramid.append(row)

    return(pyramid)

import tqdm
import math
import numpy as np
import threading
#import multiprocessing 

class calculationThread(threading.Thread):#multiprocessing.Process):
    """
    Thread calculating a part of the solution.
    TODO: modify in order to support multitheading (for the implemented version, expecting computation time divided by min(number of cores, 4))
    """
    
    def __init__(self, divisors, offset, kstart, kstop, pbar):
        super().__init__()
        self.count = 0
        self.divisors = divisors.copy()
        self.offset = offset
        self.kstart = kstart
        self.kstop = kstop
        self.pbar = pbar
    def run(self):
        for k in range(self.kstart, self.kstop):
            n = 3*k + self.offset
            divisors = n % self.divisors.copy()
            if (divisors == 0).sum() == 0:
                self.count = self.count + 1
            self.pbar.update(1)

def problem202(reflectionNumber):

    """
    Solving problem
    Computation time: ~3 hours on a recent i3 desktop processor (monothreaded program)
    """

    # Case if the reflectionNumber is 1 (then only center line is valid, it is a particular case)
    if reflectionNumber == 1:    
        return 1

    # Index of the last row
    rowCount = (reflectionNumber - 1) // 2 + 2

    # Compute the divisors of rowCount, except 1
    divisors = []
    print("Computing divisors")
    with tqdm.tqdm(total=math.floor(math.sqrt(rowCount)) - 1) as pbar:
        for i in range(2, math.floor(math.sqrt(rowCount)) + 1):
            if rowCount%i == 0:
                divisors.append(i)
                divisors.append(rowCount//i)
            pbar.update(1)
    divisors.sort()
    print(len(divisors), " divisors found")

    # For each "C" index, check if it is divisable by one of the divisors.
    # Only limit to divisors < number, so that half of the solutions are found
    #count = 0
    offset = (3 - rowCount) % 3
    kmax = (rowCount - offset) // 3

    print("Computing indexes")
    divisors = np.array(divisors)
    ksplit = ((kmax + 1)//2) // 4

    threads = []

    with tqdm.tqdm(total=(kmax + 1)//2) as pbar:
        # TODO: Part to be modified to adapt to the number of available cores
        threads.append(calculationThread(divisors, offset, 0, ksplit, pbar))
        threads.append(calculationThread(divisors, offset, ksplit, 2 *ksplit, pbar))
        threads.append(calculationThread(divisors, offset, 2 *ksplit, 3 *ksplit, pbar))
        threads.append(calculationThread(divisors, offset, 3 *ksplit, (kmax + 1)//2, pbar))
        for t in threads:
            #if __name__ == '__main__':
            #    multiprocessing.freeze_support()
            t.start()
            #t.join()
        for t in threads:
            t.join()

    count = 0
    for t in threads:
        count = count + t.count
        
    ## No thread version
    #with tqdm.tqdm(total=(kmax + 1)//2) as pbar:
    #    for k in range(0, (kmax + 1)//2):
    #        n = 3*k + offset
    #        divisorsCopy = divisors.copy()
    #        divisorsCopy = n % divisorsCopy
    #        if (divisorsCopy == 0).sum() == 0:
    #            count = count + 1
    #        pbar.update(1) 

    ## Other solution, very slow, without using numpy
    #with tqdm.tqdm(total=(kmax + 1)//2) as pbar:
    #    for k in range(0, (kmax + 1)//2):
    #        n = 3*k + offset
    #        isValid = True
    #        for j in range(0,len(divisors)):
    #            if n%divisors[j] == 0:
    #                isValid = False
    #                break
    #        if isValid:
    #            count = count + 1
    #        pbar.update(1) 

    return(count * 2)

reflectionNumber = 12017639147           

#print(buildPyramid(reflectionNumber))
print(problem202(reflectionNumber))