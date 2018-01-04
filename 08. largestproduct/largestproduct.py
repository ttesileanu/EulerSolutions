""" Find the thirteen adjacent digits in a given 1000-digit number that have the
greatest product. What is the value of this product? """

import operator
import time

with open('number.txt') as f:
  number = ''.join(line.rstrip() for line in f.readlines())

# number of adjacent digits we're interested in
n = 13

algorithm = 'trivial'

t0 = time.time()

if algorithm == 'trivial':
  prod_max = 0
  numbers_max = [0]*n
  pos_max = -1

  for i in xrange(len(number) - n + 1):
    crt_numbers = [int(c) for c in number[i:i+n]]
    crt_prod = reduce(operator.mul, crt_numbers, 1)
    if crt_prod > prod_max:
      prod_max = crt_prod
      numbers_max = crt_numbers
      pos_max = i
else:
  raise ('Unknown algorithm.')

t1 = time.time()

print 'Numbers', numbers_max, 'their product', prod_max
print '...at position', pos_max+1
print 'Took', t1 - t0, 'seconds.'
