""" How many different ways are there to make 2 pounds out of the following
    coins?
      1p, 2p, 5p, 10p, 20p, 50p, 1 pound, and 2 pounds
    (1 pound = 100p)
"""

# will assume that the target and every coin value is divisible by min(coins)
coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200

import time

t0 = time.time()

# We assumed that the target and every coin value are divisible by the smallest
# coin. This implies that we can choose arbitrary numbers of all the other
# coins, provided the sum does not exceed target, and then we simply need to
# choose the number of the smallest coins to make the sum right. This is always
# possible because of the divisibility.

coins = sorted(coins)[::-1]
counts = [0 for _ in coins]

total = 0

while counts[-1] == 0:
  k = 0
  while True:
    counts[k] += 1
    if sum(x*y for x, y in zip(coins, counts)) <= target:
      break
    else:
      counts[k] = 0
    k += 1

  total += 1

t1 = time.time()

print("Number of different ways of making {} pence with the following coins".
  format(target))
print coins
print "is {}.".format(total)

print "Took {:.2f} seconds.".format(t1 - t0)
