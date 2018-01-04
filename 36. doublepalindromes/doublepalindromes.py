""" Find the sum of all numbers under one million which are palindromic in base
10 and in base 2.

Leading zeros should not be included when deciding the palindrome property.
Example: 585 = 1001001001 (binary) is palindromic in both bases.
"""

import time
import itertools

# maximum number of digits
# XXX this should be even
digmax = 6

t0 = time.time()

def tonum(l):
  """ Make number from list of digits. """
  return reduce(lambda x, y: 10*x + y, l, 0)

def genpal(n):
  """ Generate all palindromes with at most n digits. n should be even. """
  res = []
  for k in xrange(1, n/2+1):
    # need to keep only the ones that don't end with zeros!
    all_kdigit = [l for l in itertools.product(range(10), repeat=k)
      if len(l) ==  0 or l[-1] != 0]
    # these have 2*k-1 digits
    res.extend(tonum(tuple(reversed(l)) + l[1:]) for l in all_kdigit)
    # these have 2*k digits
    res.extend(tonum(tuple(reversed(l)) + l) for l in all_kdigit)

  return res

def isbinpal(n):
  """ Check whether the number is a binary palindrome. """
  b = '{:b}'.format(n)
  return b == b[::-1]

doublesum = sum(x for x in genpal(digmax) if isbinpal(x))

t1 = time.time()

print "The sum of the double palindromes under {} is {}.".format(
  10**digmax, doublesum)
print "Took {:.2f} ms.".format(1000*(t1 - t0))
