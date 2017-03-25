#
# Created by 14chanwa on 2017.03.25
#

# Project Euler - Problem 40
# Champernowne's constant


def champernowne(n):
    """
    Builds Champernowne's sequence at least until the nth digit after the comma.
    :param n:
    :return:
    """
    sequence = '0'
    current_i = 1
    while len(sequence) < n + 1:
        sequence += str(current_i)
        current_i += 1
    return sequence

ch = champernowne(1000000)
print(int(ch[1]) * int(ch[10]) * int(ch[100]) * int(ch[1000]) * int(ch[10000]) * int(ch[100000]) * int(ch[1000000]))
