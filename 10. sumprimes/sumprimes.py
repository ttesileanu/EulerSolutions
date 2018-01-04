""" Find the sum of all the primes below two million. """

import time
import math

Nmax = 2000000

#algorithm = 'trivial'
algorithm = 'sieve'

t0 = time.time()

if algorithm == 'trivial':
  # start with a seed
  primes = [2, 3, 5, 7, 11]
  primes = [x for x in primes if x < Nmax]
  k = primes[-1] + 2
  while k < Nmax:
    div_max = int(math.sqrt(k))
    is_prime = True
    for div in primes:
      if k % div == 0:
        is_prime = False
        break
      if div > div_max:
        break

    if is_prime:
      primes.append(k)

    k += 2
elif algorithm == 'sieve':
  # prime_table[i] should be True if 2*i + 3 is prime
  prime_table = [True]*((Nmax-3) / 2)
  k_max = int(math.sqrt(Nmax))
  for k in xrange(3, k_max+1, 2):
    if prime_table[(k - 3)/2]:
      for j in xrange((k*k - 3)/2, len(prime_table), k):
        prime_table[j] = False

  primes = [2] + [2*i + 3 for (i, p) in enumerate(prime_table) if p]
else:
  raise Exception('Unknown algorithm.')

t1 = time.time()

print sum(primes)
print 'Took', t1 - t0, 'seconds.'
