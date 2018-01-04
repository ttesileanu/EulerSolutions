""" What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the 20x20 grid?
"""

import time
import numpy as np

t0 = time.time()

grid0 = np.reshape(np.fromfile('grid.txt', sep=' ', dtype=int), (20, 20))
grid = np.zeros((24, 24), dtype=int)
grid[:20, :20] = grid0

algorithm = 'naive'

if algorithm == 'naive':
  max_prod = 0
  max_numbers = []
  for i in xrange(20):
    for j in xrange(20):
      numbers = {'right': grid[i, j:j+4],
                 'down': grid[i:i+4, j],
                 'diag': grid[range(i, i+4), range(j, j+4)],
                 'rdiag': grid[range(i, i+4), range(j, j-4, -1)] if j > 4 else 0}
      prods = {name: np.prod(n) for (name, n) in numbers.iteritems()}
      crt_max = max(prods.values())
      if crt_max > max_prod:
        max_prod = crt_max
        max_numbers = numbers[[name for (name, p) in prods.iteritems()
            if p == crt_max][0]]
else:
  raise Exception('Unknown algorithm.')

t1 = time.time()

print 'Numbers:', max_numbers, ', product:', max_prod

print 'Took', t1 - t0, 'seconds.'
