""" Find the largest palindrome made from the product of two 3-digit numbers.
"""

# this will probably have 5 digits

# any palindrome with an odd number of digits is a multiple of 11, because it is
#   x = \sum_{k = 0}^{(n-1)/2} a_k*(10**k + 10**(n-k))
# but 10**(n-k) + 10**k = 10**k*(10**(n-2*k) + 1)
# and since n is odd, n-2*k is odd, and this is
#   = 10**k*(10 + 1)*(1 - 10 + 10**2 - ... + 10**(n-2*k-1))

import time
import math

def is_palindrome(n):
  """ Check whether the number is a palindrome. """
  s = str(n)
  return s == s[::-1]

def find_multiples(k, m):
  """ Find all mulitples of m with k digits. """
  lowest = int(math.ceil(10**(k-1)/m))*m
  return range(lowest, 10**k, m)

t0 = time.time()

all_multiples = find_multiples(3, 11)
all_products = [x*y for x in all_multiples for y in all_multiples]
sorted_products = sorted(all_products, reverse=True)

largest_idx = [is_palindrome(n) for n in sorted_products].index(True)
t1 = time.time()
print sorted_products[largest_idx]

print 'Took', t1 - t0, 'seconds'
