""" Find the value of d < 1000 for which 1/d contains the longest recurring
cycle in its decimal fraction part.
"""

import time

d_max = 1000

t0 = time.time()

def find_cycle(d):
  """ Find the recurring cycle for 1/d. """
  # we implement long division: start with 10, find floor(10/d) -- that's the
  # first digit; then calculate the remainder, multiply by 10, divide by d, take
  # the floor -- that's the second digits; etc.
  # once we reach a remainder that we had reached before, we stop: we have found
  # a cycle
  digits = []
  remainders = dict()
  
  rem = 1
  while not remainders.has_key(rem):
    remainders[rem] = len(digits)
    digits.append(10*rem / d)

    # new remainder
    rem = (10*rem) % d

  return digits[remainders[rem]:]

cycle_lengths = [(d, len(find_cycle(d))) for d in xrange(1, d_max)]

d_longest = max(cycle_lengths, key=lambda t: t[1])[0]

t1 = time.time()

print ("The number d such that 1/d has the longest cycle (for d < {}) is {}.".
  format(d_max, d_longest))

print "Took {:.2f} ms.".format(1000*(t1 - t0))
