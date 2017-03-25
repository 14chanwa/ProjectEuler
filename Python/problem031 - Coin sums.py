#
# Created by 14chanwa on 2017.02.12
#

# Project Euler - Problem 31
# Coin sums

availableCoinsStocks = {1:3, 2:1, 5:1, 10:0, 20:2, 50:1, 100:1, 200:0}

def getCombinationNumber(availableCoinsStocks, objective, countPieces, maxUsed):
    """
    A recursive function calculating the number of possible combinations.
    The order of the combinations is not taken into account: 50pc then 20pc is the same as 20pc then 50pc.
    maxUsed: the algorithm can not use a coin valued less than this number. This prevents the algorithm to count the same combination more than once.
    """

    combinations = 0

    # Take the quantity of coins into account
    if (countPieces):
        for key, value in availableCoinsStocks.items():
            # If there is an authorized coin in stock
            if value > 0 and key <= maxUsed:
                if objective - key > 0:
                    # Create a new inventory without the coin used at this step
                    new_availableCoinStocks = dict(availableCoinsStocks)
                    new_availableCoinStocks[key] = value - 1
                    # Recursively compute the possible combinations resulting the choice of this coin at this step
                    combinations = combinations + getCombinationNumber(new_availableCoinStocks, objective - key, countPieces, min(key, maxUsed))
                elif objective - key == 0:
                    # The objective is complete
                    combinations = combinations + 1
                # Else, no combination can be explored further
        return combinations
    # Only consider the keys (the number of coins is not limited)
    else:
        for key in availableCoinsStocks.keys():
            # If the value is authorized
            if key <= maxUsed:
                if objective - key > 0:
                    # Recursively compute the possible combinations resulting the choice of this coin at this step
                    combinations = combinations + getCombinationNumber(availableCoinsStocks, objective - key, countPieces, min(key, maxUsed))
                elif objective - key == 0:
                    # The objective is complete
                    combinations = combinations + 1
                # Else, no combination can be explored further
        return combinations
        

def problem31(availableCoinsStocks, objective, countPieces):
    """
    Checks if it is possible to attain the objective sum using the availableCoins ; if countPieces, then take the stocks into consideration.
    availableCoinsStocks: dict. key = value of the coin, value = number of coins available
    objective: int
    countPieces: bool
    """
    return getCombinationNumber(availableCoinsStocks, objective, countPieces, max(availableCoinsStocks.keys()))

print(problem31(availableCoinsStocks, 200, True))
print(problem31(availableCoinsStocks, 200, False))