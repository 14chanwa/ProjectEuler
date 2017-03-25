#
# Created by 14chanwa on 2017.02.13
#

# Project Euler - Problem 54
# Poker hands

class Card(object):
    """
    A class containing the value and family of the card, encoded in numerical values (see below)
    """

    value = 0
    family = 0

    def __init__(self, value, family):
        self.value = value
        self.family = family

class Hand(object):
    """
    A class containing the composition of the hand of the player (5 cards) along with methods to compute the value of the hand and compare two different hands.
    """
    
    def __init__(self, cards):
        """
        Creates a hand using the provided 5 cards
        cards: an array containing series of "XY" where X is a value from 2 to 10, or J, Q, K or A and Y is H, D, C or S
        """
        self.cards = []

        for i in range(0, 5):
            value = 0
            family = 0
            
            # Value of the card
            if (cards[i])[0] in "23456789":
                value = int((cards[i])[0])
            elif (cards[i])[0] == "T":
                value = 10
            elif (cards[i])[0] == "J":
                value = 11
            elif (cards[i])[0] == "Q":
                value = 12
            elif (cards[i])[0] == "K":
                value = 13
            elif (cards[i])[0] == "A":
                value = 14
            
            # Family of the card
            if (cards[i])[1] == "H":
                # Hearts
                family = 1
            elif (cards[i])[1] == "D":
                # Diamonds
                family = 2
            elif (cards[i])[1] == "C":
                # Clubs
                family = 3
            elif (cards[i])[1] == "S":
                # Spades
                family = 4
            
            self.cards.append(Card(value, family))
    
    def computeValue(self):
        """
        Computes the value of the figure
        returns: [value of the components] in a list
        The value of the components include all the elements that can help determine the winner. They have to be compared from the first to the last element.
        """
        score = []

        # The hands are ranked as follow:
        ## Royal Flush: 10
        values = []

        for card in self.cards:
            values.append(card.value)

        values.sort()

        royalFlush = [10, 11, 12, 13, 14]
        if values == royalFlush:
            score.append(10)
            return score

        ## Straight Flush: 9
        cardValuesPerFamily = ([], [], [], [])
        for card in self.cards:
            cardValuesPerFamily[card.family-1].append(card.value)
        for list in cardValuesPerFamily:
            list.sort()

        for i in range(0,4):
            # Check if consecutive values
            if len(cardValuesPerFamily[i]) == 5:
                if cardValuesPerFamily[i][4] - cardValuesPerFamily[i][0] == 4:
                    score.append(9)
                    score.append(cardValuesPerFamily[i][4])
                    return score

        ## Four of a Kind: 8
        for i in range(1,15):
            count = 0
            otherValue = 0
            for card in self.cards:
                if card.value == i:
                    count = count + 1
                else:
                    otherValue = max(otherValue, card.value)

            # count cannot be 5
            # Thus, otherValue is not 0
            if count == 4:
                score.append(8)
                score.append(i)
                score.append(otherValue)
                return score

        # Full House: 7
        pairValue = 0
        tripleValue = 0
        for i in range(1,15):
            count = 0
            for card in self.cards:
                if card.value == i:
                    count = count + 1
            # Case count = 4 - Four of a Kind - has been dealt with
            if count > 2:
                tripleValue = i
            elif count > 1:
                pairValue = i
        if pairValue > 0 and tripleValue > 0:
            score.append(7)
            score.append(tripleValue)
            score.append(pairValue)
            return score

        # Flush: 6
        for i in range(0,4):
            if len(cardValuesPerFamily[i]) == 5:
                score.append(6)
                for j in range(5, 0, -1):
                    score.append(cardValuesPerFamily[i][j-1])
                return score

        
        # Straight: 5
        isStraight = True
        for i in range(1, 5):
            if values[i] - values[i-1] != 1:
                isStraight = False
        if isStraight:
            score.append(5)
            score.append(values[4])
            return score
            

        # Three of a Kind: 4
        if tripleValue > 0:
            score.append(4)
            score.append(tripleValue)
            maxValue = 0
            for j in range(len(values), 0, -1):
                if values[j-1] != tripleValue:
                    score.append(values[j-1])
                    return score

        ## Two Pairs: 3
        ## One Pair: 2
        pairCounts = []
        
        for i in range(1,15):

            count = 0
            for card in self.cards:
                if card.value == i:
                    count = count + 1
            # Cases count = 3 or 4 have been dealt with
            if count > 1:
                pairCounts.append(i) 

        if len(pairCounts) == 2:
            # Two Pairs
            score.append(3)
            score.append(max(pairCounts[0], pairCounts[1]))
            score.append(min(pairCounts[0], pairCounts[1]))
            precValue = 0
            count = 0
            for j in range(len(values), 0, -1):
                if values[j-1] == precValue:
                    count = count + 1
                else:
                    if precValue != 0:
                        score.append(precValue)
                    precValue = values[j-1]
                    count = 1
                if count > 2:
                    score.append(precValue)
            return score

        if len(pairCounts) == 1:
            # One Pair
            score.append(2)
            score.append(pairCounts[0])
            precValue = 0
            count = 0
            for j in range(len(values), 0, -1):
                if values[j-1] == precValue:
                    count = count + 1
                else:
                    if precValue != 0:
                        score.append(precValue)
                    precValue = values[j-1]
                    count = 1
                if count > 2:
                    score.append(precValue)
            return score
        

        ## High Card: 1
        score.append(1)
        allValues = []
        for card in self.cards:
            allValues.append(card.value)

        allValues.sort()

        for i in range(len(allValues), 0, -1):
            score.append(allValues[i- 1])
        return score

    def compare(self, adverse):
        """
        Compares the hand with an adverse hand
        returns: -1 if the adverse hand wins, 1 if this hand wins, 0 if tie
        """
        selfScore = self.computeValue()
        adverseScore = adverse.computeValue()

        #print(selfScore)
        #print(adverseScore)

        for i in range(0, len(selfScore)):
                if selfScore[i] > adverseScore[i]:
                    return 1
                elif selfScore[i] < adverseScore[i]:
                    return -1      

        return 0

f = open('p054_poker.txt', 'r')
words = f.read()

wordlist = list(map(str, words.split('\n')))
print("Play count: ", len(wordlist))

count = 0
for i in range(0, len(wordlist)):
    playString = list(map(str, wordlist[i].split(' ')))
    player1 = Hand(playString[:5])
    player2 = Hand(playString[5:])
    result = player1.compare(player2)
    if result == 1:
        count = count + 1

    print(i, "-", wordlist[i], result)

print(count)

## ex 1
#player1 = Hand(["5H", "5C", "6S", "7S", "KD"])
#player2 = Hand(["2C", "3S", "8S", "8D", "TD"])
#print(player1.compare(player2))

## ex 2
#player1 = Hand(["5D", "8C", "9S", "JS", "AC"])
#player2 = Hand(["2C", "5C", "7D", "8S", "QH"])
#print(player1.compare(player2))

## ex 4
#player1 = Hand(["4D", "6S", "9H", "QH", "QC"])
#player2 = Hand(["3D", "6D", "7H", "QD", "QS"])
#print(player1.compare(player2))

#player1 = Hand(["8C", "TS", "KC", "9H", "4S"])
#player2 = Hand(["7D", "2S", "5D", "3S", "AC"])
#print(player1.compare(player2))