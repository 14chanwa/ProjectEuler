#
# Created by 14chanwa on 2017.02.22
#

# Project Euler - Problem 65
# Passcode derivation

f = open('p079_keylog.txt', 'r')

passcodes = f.read()
passcodes_list = list(map(str, passcodes.split("\n")))

# Compute a dictionnary of conditions: to each number the set of the numbers preceding it

numbers_before = {}
present_numbers = []

for i in range(0, 10):
    numbers_before[i] = set()

for passcode in passcodes_list:
    numbers_before[int(passcode[2])].add(int(passcode[0]))
    numbers_before[int(passcode[2])].add(int(passcode[1]))
    numbers_before[int(passcode[1])].add(int(passcode[0]))
    present_numbers.append(int(passcode[0]))
    present_numbers.append(int(passcode[1]))
    present_numbers.append(int(passcode[2]))

present_numbers = list(set(present_numbers))

final_passcode = []

# Assume each number appears only once!
# Look for the least restrictive digit (as for "before conditions")
# The least restrictive digit is located at the beginning of the passcode
# Once added, remove the number from the other "before conditions"

i = 0
while i < len(present_numbers):
    if len(numbers_before[present_numbers[i]]) == 0:
        element = present_numbers[i]
        final_passcode.append(element)
        for element_set in numbers_before.values():
            element_set.discard(element)
        present_numbers.remove(element)
        i = 0
    else:
        i += 1

print(final_passcode)
