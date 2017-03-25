#
# Created by 14chanwa on 2017.03.25
#

# Project Euler - Problem 43
# Sub-string divisibility

from itertools import permutations

base_string = "0123456789"
perm = [''.join(p) for p in permutations(base_string)]

total_sum = 0
for perm_str in perm:
    if int(perm_str[1:4]) % 2 == 0 and \
                            int(perm_str[2:5]) % 3 == 0 and \
                            int(perm_str[3:6]) % 5 == 0 and \
                            int(perm_str[4:7]) % 7 == 0 and \
                            int(perm_str[5:8]) % 11 == 0 and \
                            int(perm_str[6:9]) % 13 == 0 and \
                            int(perm_str[7:10]) % 17 == 0:
        total_sum += int(perm_str)

print(total_sum)
