""" Find the sum of all the multiples of 3 or 5 below 1000. """

import time

algorithm = 'naive'
#algorithm = 'inclusion_exclusion'

Nmax = 1000

t0 = time.time()

if algorithm == 'naive':
  mul3 = set(range(3, Nmax, 3))
  mul5 = set(range(5, Nmax, 5))
  numbers = set.union(mul3, mul5)
  s = sum(numbers)
elif algorithm == 'inclusion_exclusion':
  n3 = int((Nmax-1)/3)
  n5 = int((Nmax-1)/5)
  n15 = int((Nmax-1)/15)
  sum3 = 3*n3*(n3 + 1)/2
  sum5 = 5*n5*(n5 + 1)/2
  sum15 = 15*n15*(n15 + 1)/2
  s = sum3 + sum5 - sum15
else:
  raise Exception('Unknown algorithm')

t1 = time.time()

print s
print 'Took', t1 - t0, 'seconds.'
