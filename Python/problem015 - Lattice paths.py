#
# Created by 14chanwa on 2017.02.18
#

# Project Euler - Problem 015
# Lattice paths

# In order to get to the final point, tou have to go 20 times rights and 20 times down. You may choose when you go
# right or down ; deciding for instance the position of your 20 moves rights among the total 40 movement determines
# the trajectory.


from math import factorial

print(factorial(40) // (factorial(20)**2))
