""" We call an n-digit number (n < 10) '1 through n pandigital' if it makes use
of all the digits 1, ..., n exactly once. For example 15234 is 1 through 5
pandigital.

Find the sum of all products P = X x Y in which the concatenation of P, X, Y is
a 1 through 9 pandigital.

Note that some products can be obtained in more than one way, so be sure to only
include it once in the sum.
"""

import time
import itertools

t0 = time.time()

# suppose X is k-digit, Y is l-digit, and P is m-digit; then k + l + m = 9
# assuming w.l.o.g. that k <= l
# also, 10^{k-1} <= X < 10^k, 10^{l-1} <= Y < 10^l, and so, since X * Y = P,
# 10^{k + l  - 2} <= P < 10^{k + l}
# 10^{m-1} <= P < 10^m, so
# k + l - 2 < m < k + l + 1 ; m = 9 - k - l
# k + l - 2 < 9 - k - l < k + l + 1
# 2*(k + l) - 2 < 9 < 2*(k + l) + 1
# 4 < k + l < 11/2 --> k + l = 5 --> k = 1, l = 4 or k = 2, l = 3

# Simple approach: generate all 9! permutations, split them according to (k, l)
# = (1, 4) or (2, 3), find the ones that obey X * Y = P, keep track of all the
# Ps

products = set()
digits = [str(d) for d in xrange(1, 10)]
for permutation in itertools.permutations(digits):
  p = int(''.join(permutation[5:]))

  # try k = 1, l = 4
  x = int(permutation[0])
  y = int(''.join(permutation[1:5]))
  if x*y == p:
    products.add(p)

  # try k = 2, l = 3
  x = int(''.join(permutation[:2]))
  y = int(''.join(permutation[2:5]))
  if x*y == p:
    products.add(p)

t1 = time.time()

print "The sum of all the pandigital products is {}.".format(sum(products))

print "Took {:.2f} seconds.".format(t1 - t0)
