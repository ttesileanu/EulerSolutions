""" Find the sum of all the amicable numbers under 10000. """

import time
import math

N = 10000

t0 = time.time()

# first find the divisor sums for all the numbers under N
divisor_sums = [0]*N
divisor_sums[2] = 1

for n in xrange(3, N):
  # find the lowest divisor -- which will be prime
  divisor = None
  if n%2 == 0:
    divisor = 2
  else:
    p_max = int(math.sqrt(n))
    for p in xrange(3, p_max+1, 2):
      if n%p == 0:
        divisor = p
        break

  if divisor == None:
    # n is prime
    divisor_sums[n] = 1
  else:
    # find the power of this divisor
    mu = 1
    i = n/divisor
    while i%divisor == 0:
      i /= divisor
      mu += 1

    # the proper divisors of n = (p**mu)*m are all the divisors minus n
    # all the divisors of n are
    #   - all the divisors of m
    #   - all the divisors of m times p
    #   - all the divisors of m times p**2
    #     ...
    #   - all the divisors of m times p**mu
    m = n/(divisor**mu)
    m_all_div_sum = divisor_sums[m] + m
    divisor_sums[n] = sum(m_all_div_sum*divisor**i for i in xrange(mu+1)) - n

# now check for amicable numbers
amicable = [False]*N
for (n, n_div_sum) in enumerate(divisor_sums):
  # want the second number in the pair to be larger than n to avoid double
  # counting
  if n_div_sum > n and n_div_sum < N and divisor_sums[n_div_sum] == n:
    # this is a pair of amicable numbers!
    amicable[n] = True
    amicable[n_div_sum] = True

amicable_sum = sum(n for n, a in enumerate(amicable) if a)

t1 = time.time()

print "The sum of amicable numbers under {} is {}.".format(N, amicable_sum)

print "Took {:.2f} ms.".format(1000*(t1 - t0))
