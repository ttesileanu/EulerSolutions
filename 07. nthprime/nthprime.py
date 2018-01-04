""" What is the 10001st prime number? """

import math
import time

n = 10001

t0 = time.time()

#algorithm = 'trial_division'
algorithm = 'eratosthenes'

# have some "seed" primes
if algorithm == 'trial_division':
  primes = [2, 3, 5, 7, 11, 13]
  k = primes[-1] + 2
  while len(primes) < n:
    isprime = True
    m_max = int(math.sqrt(k))
    for m in primes:
      if k % m == 0:
        isprime = False
        break
      elif m > m_max:
        break
    if isprime:
      primes.append(k)

    k += 2

  nth_prime = primes[n-1]
elif algorithm == 'eratosthenes':
  # estimate size of nth prime
  if n >= 6:
    nth_prime_approx = int(math.ceil(n*math.log(n) + n*math.log(math.log(n))))
  else:
    nth_prime_approx = 2*n + 2
  # sieve[k] is whether 2*k + 3 is prime
  sieve = [True]*(nth_prime_approx / 2)
  sieve_max = len(sieve)
  k_max = int(math.sqrt(nth_prime_approx))
  for k in xrange(3, k_max+1, 2):
    if sieve[(k - 3)/2]:
      for j in xrange((k*k - 3)/2, sieve_max, k):
        sieve[j] = False

  # find the nth prime
  k = 1
  for (i, isprime) in enumerate(sieve):
    if isprime:
      k += 1
    if k == n:
      nth_prime = 2*i + 3
      break
else:
  raise Exception('Unknown algorithm')

t1 = time.time()

print nth_prime
print 'Took', t1 - t0, 'seconds.'
