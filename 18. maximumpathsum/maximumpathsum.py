""" By starting at the top of the triangle in triangle.txt and moving to
adjacent numbers on the row below, what is the maximum total sum from top to
bottom?

Note: a number at position i in a row is adjacent to numbers at positions i and
i+1 in the row below.
"""

import time

t0 = time.time()

# load the data
with open('triangle.txt', 'r') as f:
  triangle = []
  for row in f:
    triangle.append([int(x) for x in row.split()])

# We calculate the path with the largest sum if we started in every position of
# the triangle. If we know the largest sums for all the positions in row i, then
# the largest sums for positions in row i-1 can be obtained by simply finding
# which sum is larger -- the one where we choose to move left from row i-1 to i,
# or the one where we choose to move right. We can thus iterate through the rows
# from the bottom up until we find the largest path starting at the top of the
# triangle.

largest_sums = [0]*(len(triangle[-1]) + 1)
for row in reversed(triangle):
  largest_sums = [n + max(largest_sums[i], largest_sums[i+1])
                  for i, n in enumerate(row)]

t1 = time.time()

print "Largest sum is {}.".format(largest_sums[0])

print "Took {:.2f} ms.".format(1000*(t1 - t0))
