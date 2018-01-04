""" Form a spiral by starting in the middle of an n x n square (with n odd) and
moving clockwise. Fill the spirals with increasing integers, starting at 1. For
example, for n = 5, we have

    21 22 23 24 25 
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

Find the sum of the numbers on the diagonals in a 1001 x 1001 spiral formed in
this way.
"""

import time

n = 1001

t0 = time.time()

# The spiral is essentially built one square at a time, first size 1, then size
# 3, then size 5, etc. The values we need to add are the values in the corners
# of these intermediate squares. These values always go in an arithmetic
# progression; for size 3, the step is 2; for size 5, the step is 4; for size 7,
# the step is 6; etc. (for size n, the step is n - 1).
# The difference between the last value at size n and the first value at size
# n + 2 is n + 1. The starting value at size 1 is 1; at size 3 is 3; at size 5
# is 13; at size 7 is 31; at size 9 is 57; ...
# If we call the starting value at size n a_n, we have
#   a_{n+2} = a_n + 4*(n-1) + 2 = a_n + 4*n - 2
# and thus
#   a_n = n**2 -3*n + 3
# This means that the sum of the corners of the square of size n (n > 1!) is
#   4*a_n + (1 + 2 + 3)*(n - 1) = 4*a_n + 6*(n - 1) = 4*n**2 - 6*n + 6
# So the sum we are interested in is
#   1 + \sum_{k = 3, ..., n} (4*k**2 - 6*k + 6) = 
#     = (4*n**3 + 3*n**2 + 8*n + 15)/6

diag_sum = (4*n**3 + 3*n**2 + 8*n - 9)/6

t1 = time.time()

print "The sum of the diagonal elements in the {0}x{0} spiral is {1}.".format(
  n, diag_sum)

print "Took {:.2f} us.".format(1000000*(t1 - t0))
