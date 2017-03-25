#
# Created by 14chanwa on 2017.03.25
#

# Project Euler - Problem 33
# Digit cancelling fractions


# A possible algorithm...
# Given a 2-digit denominator, consider all 2-digit numerators inferior to the denominator having at least one digit in
# common with the denominator. Cancelling the possible digits, check if the value of the fraction is the same (reducing
# the fraction to its minimal form).

from fractions import Fraction

digit_cancelling_fractions = set()

for den in range(11, 100):
    for num in range(10, den):
        str_num = str(num)
        str_den = str(den)

        # Find common digits (could have 2 common digits)
        common_digits = set()
        for d in str_num:
            if d in str_den:
                if d != '0':
                    common_digits.add(d)

        # print(str_num, str_den, common_digits)

        if len(common_digits) > 0:

            # For each common digit, remove one occurrence and check whether the fraction is the same as the original
            for d in common_digits:
                new_str_num = ''.join([a for a in str_num if a != d])
                new_str_den = ''.join([a for a in str_den if a != d])

                # Handle the case: two same digits
                if len(new_str_num) == 0:
                    new_str_num = d
                if len(new_str_den) == 0:
                    new_str_den = d

                new_num = int(new_str_num)
                new_den = int(new_str_den)

                # If the new fraction is equal to the starting fraction, memorize
                if new_den > 0 and Fraction(new_num, new_den) == Fraction(num, den):
                    digit_cancelling_fractions.add(Fraction(num, den))
                    # print(new_num, new_den, num, den)


# print(digit_cancelling_fractions)

total_fraction = Fraction(1)
for fraction in digit_cancelling_fractions:
    total_fraction *= fraction

print(total_fraction)
