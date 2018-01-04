""" What is the millionth lexicographic permutation of 0, ..., 9? """

import time

# number of objects
N = 10
# which permutation we're interested in (1-based)
n1 = 1000000

t0 = time.time()

# the permutation we're interested in (0-based)
n = n1 - 1

# To generate permutations in lexicographic order, we note that all the
# permutations starting with i+1 come after all of the ones starting with i.
# Thus generating all permutations of size N is equivalent to choosing the first
# number, and then for each choice generate all the permutations with N-1
# objects.

# What this means is that the (n+1)th permutation in lexicographic order will
# have first digit given by n/(N-1)!. We can then iterate this to find the
# subsequent digits.

# keeping track of digits that we haven't yet chosen
digits_left = range(N)

# this is the permutation
perm = []

# number of possible permutations of the remaining digits
N_left = reduce(lambda x, y: x*y, xrange(1, N+1), 1)

while len(perm) < N:
  N_left /= (N - len(perm))
  first_digit = digits_left[n/N_left]
  perm.append(first_digit)
  digits_left.remove(first_digit)

  n = n%N_left

t1 = time.time()

print "The {}th permutation is {}.".format(n1, perm)

print "Took {:.2f} us.".format(1000000*(t1 - t0))
