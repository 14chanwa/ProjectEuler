#
# Created by 14chanwa on 2017.03.24
#

# Project Euler - Problem 30
# Digit fifth powers

# We are subjected to the inequality: n * 9**5 > 10**n (maximize the two members of the equality)
# An upper (included) bound of the eligible numbers is:
n_max = 1
while 10 ** n_max / n_max < 9 ** 5:
    n_max += 1
print(n_max)

# Enumerate all possibilities removing all digits with less than 2 non-zero digits (it is not a "sum").
count = 0
for n in range(1, 10 ** n_max):
    s = str(n)
    if len([a for a in s if a != '0']) > 2:
        tmp = 0
        for i in range(0, len(s)):
            tmp += int(s[i]) ** 5
        if tmp == n:
            count += n

print(count)
