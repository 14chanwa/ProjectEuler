#
# Created by 14chanwa on 2017.02.18
#

# Project Euler - Problem 013
# Large sum

f = open('p019_numbers.txt', 'r')
numbers = f.read()

numberslist = list(map(str, numbers.split('\n')))

digits = []
sum = 0
for i in range(50):
    for j in range(100):
        sum += int(numberslist[j][50 - 1 - i])
    digits.append(sum - (sum - sum % 10))
    sum //= 10

while(sum // 10 != 0):
    digits.append(sum - (sum - sum % 10))
    sum //= 10

digits.append(sum)

result = ""
for i in range(10):
    result += str(digits[len(digits) - 1 - i])
print(digits)
print(result)