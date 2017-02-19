#
# Created by 14chanwa on 2017.02.18
#

# Project Euler - Problem 89
# Roman numerals

f = open('p089_roman.txt', 'r')

words = f.read()
word_list = list(map(str, words.split("\n")))

mapping_inferior = {
    "M": "DCLXVI",
    "D": "CLXVI",
    "C": "LXVI",
    "L": "XVI",
    "X": "VI",
    "V": "I",
    "I": []
}

mapping_superior = {
    "M": [],
    "D": "M",
    "C": "MD",
    "L": "MDC",
    "X": "MDCL",
    "V": "MDCLX",
    "I": "MDCLXV"
}


def parse_sequences(word, mapping_inferior=mapping_inferior, mapping_superior=mapping_superior):
    sequences = []
    if len(word) == 0:
        return []

    new_sequence = True
    current_sequence = []
    preceding_letter = ''
    for i in range(0, len(word)):
        if new_sequence:
            current_sequence = [word[i]]
            preceding_letter = word[i]
            new_sequence = False
        else:
            current_letter = word[i]

            # Case preceding letter < current letter
            if preceding_letter in mapping_inferior[current_letter]:
                current_sequence.append(current_letter)
                sequences.append(current_sequence)
                new_sequence = True
            # Case preceding letter > current letter
            elif preceding_letter in mapping_superior[current_letter]:
                sequences.append(current_sequence)
                current_sequence = [current_letter]
                preceding_letter = current_letter
            # Case preceding letter == current letter
            elif preceding_letter == current_letter:
                current_sequence.append(current_letter)

    # End of line
    if len(current_sequence) > 0 and not new_sequence:
        sequences.append(current_sequence)

    return sequences

# for index in range(0, 20):
#     print(word_list[index])
#     print(parse_sequences(word_list[index]))

mapping_superior_unit = {
    "D":"M",
    "C":"D",
    "L":"C",
    "X":"L",
    "V":"X",
    "I":"V"
}


def arrange_sequences(sequences, mapping_superior_unit=mapping_superior_unit):
    i = 0
    while i < len(sequences):
        # Case 4 same digits in a row
        if len(sequences[i]) == 4:
            # If "M", nothing to do
            if not sequences[i][0] == "M":
                superior_unit = mapping_superior_unit[sequences[i][0]]
                if i > 0:
                    # Case [X, X, V] [I, V] for instance
                    if sequences[i-1][-1] == superior_unit:
                        sequences[i] = [sequences[i][0], mapping_superior_unit[superior_unit]]
                        if len(sequences[i-1]) == 1:
                            del sequences[i-1]
                        else:
                            del (sequences[i-1])[-1]
                            i += 1
                    else:
                        new_sequence = [sequences[i][0], mapping_superior_unit[sequences[i][0]]]
                        sequences[i] = new_sequence
                        i += 1
                else:
                    new_sequence = [sequences[i][0], mapping_superior_unit[sequences[i][0]]]
                    sequences[i] = new_sequence
                    i += 1
            else:
                i += 1
        else:
            i += 1

    return sequences


def get_decimal_value(letter):
    if letter == "M":
        return 1000
    elif letter == "D":
        return 500
    elif letter == "C":
        return 100
    elif letter == "L":
        return 50
    elif letter == "X":
        return 10
    elif letter == "V":
        return 5
    else:
        return 1


def sequences_to_decimal(sequences):
    result = 0
    for sequence in sequences:
        if len(sequence) != 2:
            result += get_decimal_value(sequence[0]) * len(sequence)
        else:
            if sequence[0] == sequence[1]:
                result += get_decimal_value(sequence[0]) * 2
            else:
                result += get_decimal_value(sequence[1]) - get_decimal_value(sequence[0])
    return result


def sequences_to_string(sequences):
    result = ''
    for sequence in sequences:
        tmp = ''
        for letter in sequence:
            tmp += letter
        result += tmp
    return result


count = 0
count_reduced = 0
for word in word_list:

    parsed_sequence = parse_sequences(word)
    for seq in parsed_sequence:
        count += len(seq)

    sequences = arrange_sequences(parsed_sequence)
    for seq in sequences:
        count_reduced += len(seq)


print(count - count_reduced)
