""" Find the sum of all curious numbers -- the numbers which are equal to the
sum of the factorials of their digits (excluding 1 = 1! and 2 = 2!).
"""

import time
import itertools

t0 = time.time()

# Suppose the number n has k digits. Then 10^{k-1} <= n < 10^k.
# The sum of k digit factorials is <= k*9!.
# So, n = sum of factorials of digits implies n <= k*9!. Since n has k digits,
# we also have n >= 10^{k-1}, so
#   10^{k-1} <= n <= k*9! --> 10^{k-1} < k*9!

# The derivative of 10^{k-1} - k*9! is ln(10)*10^{k-1} - 9!, which is negative
# for k -> -\infty, positive as k -> \infty, and vanishes at k = 6.198.

# 10^{k-1} > k*9! for k > 7.431.

# So we only need to worry about numbers with up to 7 digits.

# (another way to see this: if k = 8, 10^{k-1} = 10^7 > k*9! = 2.9*10^6)
# (for k = 7, 10^{k-1} = 10^6 < k*9! = 2.5*10^6)

# 1-digit numbers are excluded by definition

# Brute-force: enumerate all possible digit-factorial sums (this is better
# because we can take advantage of commutativity).

# precalculate factorials
factorials = [1]
for i in xrange(1, 10):
  factorials.append(factorials[i-1]*i)

curious = []
for k in xrange(2, 8):
  # the first element is all zeros, which we don't care about
  totest = list(itertools.combinations_with_replacement(xrange(10), k))[1:]

  # calculate the factorial sums for all of these
  facsums = [sum(factorials[d] for d in l) for l in totest]

  # which sums can be written with the same set of digits (incl multiplicities)?
  facsum_digits = [tuple(sorted(int(c) for c in str(n))) for n in facsums]

  curious.extend(n for n, d1, d2 in
    itertools.izip(facsums, totest, facsum_digits) if d1 == d2)

  print len(totest)

t1 = time.time()

#print curious
print "The sum of all curious numbers is {}.".format(sum(curious))

print "Took {:.2f} seconds.".format(t1 - t0)
