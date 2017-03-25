#
# Created by 14chanwa on 2017.03.21
#

# Project Euler - Problem 25
# 1000-digit Fibonacci number

# The Fibonacci sequence is given by F(n) = F(n-1) + F(n-2) for n >= 2 and F(0) = F(1) = 1.
# In fact, we can solve this linear equation: the nth term of the Fibonacci sequence is given by:
# F(n) = (1/sqrt(5))  * (phi**n - phi**(-n) ) where phi = (1 + sqrt(5)) / 2.
# Since phi**(-1) < 1, phi**(-n) -> 0 when n -> +infty, so F(n) -> (phi**n)/sqrt(5) for n -> infty.

# We want n so that: (phi**n)/sqrt(5) <= 10**999 and (phi**(n+1))/sqrt(5) > 10**999.
# In order to avoid to compute large numbers, we solve the equation and find

import math

n = (math.log(math.sqrt(5)) + 999 * math.log(10)) / math.log((1 + math.sqrt(5)) / 2)

# i.e. n ~ 4781.8592...
# Since phi**(-1) ~ 0.62... ~ 6 * 10**(-1), we have phi**(-n) ~ 10**(-4781) << 1. 

# Thus we have found n = 4782.
print(math.ceil(n))
