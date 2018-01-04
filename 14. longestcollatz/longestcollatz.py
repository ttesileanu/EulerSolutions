""" Consider the Collatz sequence: x_n is positive integer, and

    x_{n+1} = | x_n/2     if x_n is even
              | 3*x_n+1   if x_n is odd

    with the condition that the sequence ends when x_n = 1. Given x_0 < 1000000,
    what is the longest Collatz sequence?
"""

import time

N_max = 1000000

t0 = time.time()

# keep track of any sequence lengths that we already calculated
chain_lengths = {1: 1}

for x0 in xrange(1, N_max):
  # we might have already calculated this
  if not chain_lengths.has_key(x0):
    chain = [x0]
    x = x0
    while True:   # this will reach 1 eventually, and 1 is in chain_lengths
      x = x/2 if x%2 == 0 else 3*x+1

      if chain_lengths.has_key(x):
        # we already know what happens from here
        known_length = chain_lengths[x]
        break

      chain.append(x)

    # store the lengths for all the sequences we have found
    for (i, x) in enumerate(chain):
      chain_lengths[x] = len(chain) - i + known_length

below_N_max = ((i, x) for i, x in chain_lengths.items() if i < N_max)
argmax_len, max_len = max(below_N_max, key=lambda item: item[1])

t1 = time.time()

print "Starting with {} yields the longest Collatz sequence ({} terms)".format(
      argmax_len, max_len)

print "The calculation took {:.2f} seconds.".format(t1 - t0)

#print "Here's the chain:"
#x = argmax_len
#while x != 1:
#  print '{}, '.format(x),
#  x = x/2 if x%2 == 0 else 3*x+1

#print 1
