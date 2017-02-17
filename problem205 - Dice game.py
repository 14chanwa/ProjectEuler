#
# Created by 14chanwa on 2017.02.14
#

# Project Euler - Problem 205
# Dice game

fourSided = [1, 2, 3, 4]
sixSided = [1, 2, 3, 4, 5, 6]

def rollDice(possibleValues, remainingRolls, result, startSum = 0):
    """
    Rolls a dice of faces equally probable and valued possibleValues, remainingRolls times and store the possible sums of the rolls in the provided list result. Adds startSum to all the results.
    """
    if remainingRolls == 0:
        result.append(startSum)
    else:
        for value in possibleValues:
            rollDice(possibleValues, remainingRolls - 1, result, startSum + value)

import tqdm

def problem205():

    # Compute all possible sums of dice

    fourSidedResult = []
    sixSidedResult = []

    rollDice(fourSided, 9, fourSidedResult)
    rollDice(sixSided, 6, sixSidedResult)

    fourSidedResult.sort()
    sixSidedResult.sort()

    # For each value of the four sided sum, compute the probability that the six sided sum is strictly inferior

    probability = 0.0
    
    with tqdm.tqdm(total=len(fourSidedResult)) as pbar:
        startIndex = 0
        for valueFour in fourSidedResult:
            # Count the number of six sided sums below value
            # Start i from the previous value for which valueFour > sixSidedResult[i]
            for i in range(startIndex, len(sixSidedResult)):
                if sixSidedResult[i] >= valueFour :
                    probability = probability + (1.0 * i) / len(sixSidedResult)
                    startIndex = max(0, i - 1)
                    break
            else:
                probability = probability + 1.0
            
            pbar.update(1)

    probability = probability / len(fourSidedResult)
    return probability

print(problem205())