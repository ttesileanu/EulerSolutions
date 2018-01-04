""" A number is called a circular prime if all rotations of its digits form
prime numbers. An example is 197, since 197, 971, and 719 are all prime. All the
circular primes below 100 are 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97.

How many circular primes are there below one million?
"""

import time
import itertools
import math

max_digits = 6

t0 = time.time()

def is_prime(n):
  if n <= 1:
    return False

  if n % 2 == 0:
    return False

  m = int(math.sqrt(n))
  for i in xrange(3, m+1, 2):
    if n % i == 0:
      return False

  return True

def rotate(l, n):
  """ Rotate a list by n positions. """
  return l[n:] + l[:n]

def check_all_rot_prime(l):
  """ Check that all rotations of a list of digits lead to prime numbers. """
  for n in xrange(len(l)):
    rotated_number = reduce(lambda x, y: 10*x + y, rotate(l, n), 0)
    if not is_prime(rotated_number):
      return False

  return True

# Circular primes with more than one digit have to be made from the digits
# 1, 3, 7, 9. This is because numbers ending in even digits or in 5 are
# divisible by 2 or 5, respectively, and a number containing an even digit or 5
# is guaranteed to have that digit in the last position in one of the rotations.

count = 2         # 2 and 5 are circular primes, but we do not generate them
all_results = [2, 5]
for n in xrange(1, max_digits+1):
  all_ndigit = itertools.product([1, 3, 7, 9], repeat=n)

  ndigit_results = [x for x in all_ndigit if check_all_rot_prime(x)]
  all_results.extend(ndigit_results)
  count += len(ndigit_results)

t1 = time.time()

print "There are {} circular primes under {}.".format(count, 10**max_digits)

print "Took {:.2f} seconds.".format(t1 - t0)
