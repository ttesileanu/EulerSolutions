""" Consider quadratics of the form n**2 + a*n + b, with |a|, |b| < 1000. Find
the quadratic that produces the maximum number of primes for consecutive values
of n, starting with n = 0 (i.e., plugging n = 0, ..., n_max-1 in n**2 + a*n + b
yields prime numbers, and n_max**2 + a*n_max + b is not prime).

Hint: n**2 + n + 41 gives primes for n = 0 to 39.
"""

a_max = 1000
b_max = 1000

import time
import math

t0 = time.time()

# Since we need to get a prime when n = 0, b has to be prime (and thus positive)
# n**2 + a*n + b is certainly not prime when n = b (it's equal to b*(a+b+1)),
# *except* if a = -b. However, if a = -b, the value when n = 1 is 1 - b + b = 1,
# which is not prime.

# Thus, we can assume that even for the longest streak, n < b. The largest prime
# we might find is thus smaller than b_max**2 + |a_max|*b_max + b_max =
# b_max*(|a_max| + b_max + 1).

p_max = b_max*(abs(a_max) + b_max + 1)

# using Eratosthenes' sieve to find the primes we maybe interested in
sieve = [True]*(p_max + 1)
sieve[0] = False
sieve[1] = False
k_max = int(math.sqrt(p_max))
for k in xrange(2, k_max):
  if sieve[k]:
    for j in xrange(k*k, p_max, k):
      sieve[j] = False

small_primes = [p for p, b in enumerate(sieve[:b_max]) if b]

# iterate through all the values...
n_max = 0
ab_max = (0, 0)
for a in xrange(-a_max+1, a_max):
  for b in small_primes:
    for n in xrange(b):
      if not sieve[n**2 + a*n + b]:
        break
      if n > n_max:
        n_max = n
        ab_max = (a, b)

t1 = time.time()

print "The quadratic n**2 + {}*n + {} produces {} primes.".format(
  ab_max[0], ab_max[1], n_max)
print "The product of the coefficients a*b is {}.".format(ab_max[0]*ab_max[1])

print "Took {:.2f} seconds.".format(t1 - t0)
