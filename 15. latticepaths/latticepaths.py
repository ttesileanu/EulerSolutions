""" Starting in the top left corner of a 2x2 grid and only being able to move
to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20x20 grid?
"""

import time

t0 = time.time()

N = 20

# Since each step either increases x coordinate by 1 or increases y coordinate
# by 1, and each of the coordinates has to increase from 0 to N, and we are not
# allowed to step outside the boundaries, each possible path is always made up
# of exactly 2*N steps. Moreover, exactly N of these steps have to be in the x
# direction, and exactly N in the y direction. Therefore, the number of possible
# paths is the number of ways in which we can choose which N of the 2*N steps
# should be in the x direction, i.e., 2*N choose N.

# fortunately Python's long can grow indefinitely, otherwise we would have to be
# more careful in calculating our products

num = 1
denom = 1
for i in xrange(1, N+1):
  # denominator should just be N!
  denom *= i
  # numerator should be (2*N)*(2*N - 1)*...*(N+1)
  num *= N + i

t1 = time.time()

if num % denom != 0:
  print 'ERROR: result is not integer!'

print 'Number of paths in {0}x{0} grid is {1}.'.format(N, num/denom)

print "Took {:.0f} us.".format(1000000*(t1 - t0))
