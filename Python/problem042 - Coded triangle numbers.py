#
# Created by 14chanwa on 2017.02.12
#

# Project Euler - Problem 42
# Coded triangle numbers


f = open('p042_words.txt', 'r')
words = f.read()

wordlist = list(map(str, words.split(',')))
# Removing double commas
for i in range(0, len(wordlist)):
    wordlist[i] = (wordlist[i])[1:-1]

# wordlist is a list of words in the dictionnary

alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13,
            'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
            'Z': 26}


def problem42(wordlist, alphabet):
    """
    Counts the number of 'triangle words' in the provided wordlist (list).
    The alphabet consists in a dictionnary mapping letters and positions.
    """
    count = 0

    # Calculate the maximum triangle number that could be in the dictionnary
    maxLength = 0
    for i in range(0, len(wordlist)):
        maxLength = max(maxLength, len(wordlist[i]))
    maxNumber = maxLength * len(alphabet)

    # List possible triangle numbers
    triangleList = []
    n = 0
    while n * (n + 1) // 2 < maxNumber + 1:
        triangleList.append(n * (n + 1) // 2)
        n = n + 1

    # Check all words
    for word in wordlist:
        number = 0
        for letter in word:
            number = number + alphabet[letter]
        if number in triangleList:
            count = count + 1
            print(word)

    return count


print(problem42(wordlist, alphabet))
