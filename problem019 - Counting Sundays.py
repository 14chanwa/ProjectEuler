#
# Created by 14chanwa on 2017.03.18
#

# Project Euler - Problem 19
# Counting Sundays

def is_leap_year(year):
	"""
	Checks if a given year is a leap year.
	:param year:
	"""
	if year % 400 == 0:
		return True
	if year % 4 == 0:
		if year % 100 == 0:
			return False
		return True
	return False

def get_number_days(year, month):
	"""
	Gets the number of days in a given month of a given year.
	:param year:
	:param month:
	"""
	if month == 4 or month == 6 or month == 9 or month == 11:
		return 30
	elif month == 2:
		if is_leap_year(year):
			return 29
		else:
			return 28
	else:
		return 31
	
year_count = 1900
month_count = 1
day_count = 7

sunday_count = 0

# Go from monday to monday from the given date (first sunday of 1900)
# Start counting in 1901
while year_count < 2001:
	day_count += 7
	day_count_limit = get_number_days(year_count, month_count)
	if day_count > day_count_limit:
		day_count = day_count - day_count_limit  
		month_count += 1
		if month_count > 12:
			month_count = 1	
			year_count += 1
	if day_count == 1 and year_count > 1900:
		sunday_count += 1
		print(day_count, "/", month_count, "/", year_count)

print(sunday_count)
