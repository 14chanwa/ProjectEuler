#
# Created by 14chanwa on 2017.03.18
#

# Project Euler - Problem 17
# Number letter counts

def number_of_letters_digit(n):
	# Assume 0 <= n <= 9 
	if n == 0:
		return 0
	if n == 1 or n == 2 or n == 6:
		return 3
	if n == 4 or n == 5 or n == 9:
		return 4
	if n == 3 or n == 7 or n == 8:
		return 5
	
def number_of_letters_below_hundred(n):
	if n < 10:
		return number_of_letters_digit(n)
	# Assume 10 <= n <= 19
	if n == 10:
		return 3
	if n == 11 or n == 12:
		return 6
	if n == 15 or n == 16:
		return 7
	if n == 13 or n == 14 or n == 18 or n == 19:
		return 8
	if n == 17:
		return 9
	# Assume 20 <= n <= 99
	tens = n // 10
	units = n % 10
	if tens == 4 or tens == 5 or tens == 6 :
		return 5 + number_of_letters_digit(units)
	if tens == 2 or tens == 3 or tens == 8 or tens == 9:
		return 6 + number_of_letters_digit(units)
	if tens == 7:
		return 7 + number_of_letters_digit(units)		

def number_of_letters_below_thousand(n):
	# Assume n <= 1000
	if n == 1000:
		# one thousand
		return 11
	if n < 100:
		return number_of_letters_below_hundred(n)
	
	current_n = n
	quot = current_n // 100
	current_n = current_n % 100
	# hundreds
	tmp_count = number_of_letters_digit(quot) + 7
	# case ends
	if current_n == 0:
		return tmp_count
	# count remaining number
	else:
		return tmp_count + 3 + number_of_letters_below_hundred(current_n)

total_count = 0
for i in range(1, 1001):
	tmp = number_of_letters_below_thousand(i)
	print(i, ": ", tmp)
	total_count += tmp
print(total_count)
