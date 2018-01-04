""" A number n is called abundant if the sum of its proper divisors exceeds n.
The smallest abundant number is 12. It can be shown that all integers greater
than 28123 can be written as a sum of two abundant numbers.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
"""

import time
import math

t0 = time.time()

# numbers >= threshold guaranteed to be writable as sum of 2 abundant numbers
threshold = 28124

# let us start by finding all the abundant numbers < threshold
# first find the divisor sums for all the numbers under threshold
divisor_sums = [0]*threshold
divisor_sums[2] = 1

for n in xrange(3, threshold):
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

# now find all the numbers n for which divisor_sums[n] > n
is_abundant = [div_sum > n for n, div_sum in enumerate(divisor_sums)]
# the abundants list will be automatically sorted
abundants = [n for n, b in enumerate(is_abundant) if b]

# find all sums of abundant numbers that are < threshold
writeable_as_sum = [False]*threshold

for i, n1 in enumerate(abundants):
  if n1 > threshold/2:
    continue
  for n2 in abundants[i:]:
    n = n1 + n2
    if n < threshold:
      writeable_as_sum[n] = True

#print is_abundant[:12]
#print is_abundant[12]
#print sum(is_abundant)

t1 = time.time()

print(("There are {} numbers that cannot be written as a sum of two abundant " +
      "numbers below {}.").format(sum(not b for b in writeable_as_sum),
        threshold))
print("The sum of these numbers is {}.".format(sum(
          n for n, b in enumerate(writeable_as_sum) if not b)))

print "Took {:.2f} seconds.".format(t1 - t0)
