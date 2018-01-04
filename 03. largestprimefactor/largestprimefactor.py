""" What is the largest prime factor of the number 600851475143? """

import math
import time

n = 600851475143
factors = []

t0 = time.time()
while n > 1:
  if n % 2 == 0:
    factors.append(2)
    n /= 2
  else:
    k_max = int(math.sqrt(n))
    is_prime = True
    for k in xrange(3, k_max+1, 2):
      if n % k == 0:
        factors.append(k)
        n /= k
        is_prime = False
        break
    if is_prime:
      factors.append(n)
      n /= n

t1 = time.time()

print factors[-1]
print 'Took', t1 - t0, 'seconds.'
