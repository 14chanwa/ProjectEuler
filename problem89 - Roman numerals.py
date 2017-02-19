#
# Created by 14chanwa on 2017.02.18
#

# Project Euler - Problem 89
# Roman numerals

f = open('p009_roman.txt', 'r')

words = f.read()
word_list = list(map(str, words.split("\n")))


def parse_sequences(word):
    sequences = []
    if len(word) == 0:
        return []

    mapping_inferior = {
        "M": "DCVXI",
        "D": "CVXI",
        "C": "VXI",
        "V": "XI",
        "X": "I",
        "I": []
    }

    mapping_superior = {
        "M": [],
        "D": "M",
        "C": "MD",
        "V": "MDC",
        "X": "MDCV",
        "I": "MDCVX"
    }

    new_sequence = True
    current_sequence = []
    preceding_letter = ''
    for i in range(0, len(word)):
        if new_sequence:
            current_sequence = [word[i]]
            preceding_letter = word[i]
            new_sequence = False
            break

        current_letter = word[i]

        # Case preceding letter < current letter
        if preceding_letter in mapping_inferior[current_letter]:
            current_sequence.append(current_letter)
            sequences.append(current_sequence)
            new_sequence = True
        # Case preceding letter > current letter
        elif preceding_letter in mapping_superior:
            current_sequence
