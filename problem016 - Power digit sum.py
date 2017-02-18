#
# Created by 14chanwa on 2017.02.18
#

# Project Euler - Problem 16
# Power digit sum

digit_table = [1]
for i in range(1, 1001):

    for index in range(0, len(digit_table)):
        digit_table[index] *= 2

    for index in range(0, len(digit_table) - 1):
        digit_table[index + 1] += digit_table[index] // 10
        digit_table[index] %= 10

    if digit_table[len(digit_table) - 1] // 10 > 0:
        tmp = digit_table[len(digit_table) - 1]
        digit_table[len(digit_table) - 1] = tmp % 10
        digit_table.append(tmp // 10)

    print(i, digit_table)


print(digit_table)
sum = 0
for i in range(len(digit_table)):
    sum += digit_table[i]
print(sum)
