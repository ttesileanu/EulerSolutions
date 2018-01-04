""" Find the sum of all the 11 primes that are both truncatable from left to
right and from right to left.

A prime is truncatable from left to right (or right to left) if removing digits
from left to right (or right to left) yields only primes.

For example, 3797 is truncatable from both sides: 3797, 797, 97, and 7 are all
primes, as are 3797, 379, 37, and 3.

Note: Do not count 2, 3, 5, and 7 as truncatable primes.
"""

import time
import math

t0 = time.time()

def is_prime(n):
  if n == 1:
    return False

  if n % 2 == 0:
    return False

  for p in xrange(3, int(math.sqrt(n)) + 1, 2):
    if n % p == 0:
      return False

  return True

def gen_rl_trunc(n):
  """ Generate list of right-to-left truncatable primes that are obtained by
  adding one digit to the right of n.
  """
  candidates = [10*n + d for d in xrange(1, 10, 2)]
  return [newn for newn in candidates if is_prime(newn)]

def gen_all_rl(n):
  """ Generate all right-to-left truncatable primes up to n digits.

  n should be >= 2
  """
  if n < 2:
    raise Exception("gen_all_rl only works with n >= 2.")

  crt = [num for d in [2, 3, 5, 7] for num in gen_rl_trunc(d)]
  res = crt
  for i in xrange(3, n+1):
    crt = [num for d in crt for num in gen_rl_trunc(d)]
    res.extend(crt)

  return res

def is_lr_trunc(n):
  """ Check whether n is left-to-right truncatable. """
  while n > 0:
    if not is_prime(n):
      return False
    n %= 10**math.floor(math.log10(n))

  return True

two_sided = [p for p in gen_all_rl(8) if is_lr_trunc(p)]

t1 = time.time()

print "The sum of all two-sided primes is {}.".format(sum(two_sided))

print "Took {:.2f} ms.".format(1000*(t1 - t0))
